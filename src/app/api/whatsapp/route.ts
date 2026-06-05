import { NextRequest, NextResponse } from 'next/server';
import { GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { createClient } from '@supabase/supabase-js';

// Initialize Supabase Client
const supabaseUrl = process.env.SUPABASE_URL || '';
const supabaseKey = process.env.SUPABASE_ANON_KEY || '';
const supabase = createClient(supabaseUrl, supabaseKey);

function cosineSimilarity(vecA: number[], vecB: number[]) {
    let dotProduct = 0, normA = 0, normB = 0;
    for (let i = 0; i < vecA.length; i++) {
        dotProduct += vecA[i] * vecB[i];
        normA += vecA[i] * vecA[i];
        normB += vecB[i] * vecB[i];
    }
    return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
}

export async function GET(req: NextRequest) {
    const { searchParams } = new URL(req.url);
    const mode = searchParams.get('hub.mode');
    const token = searchParams.get('hub.verify_token');
    const challenge = searchParams.get('hub.challenge');

    const VERIFY_TOKEN = process.env.WHATSAPP_VERIFY_TOKEN || 'my_secure_verify_token_123';

    if (mode && token) {
        if (mode === 'subscribe' && token === VERIFY_TOKEN) {
            return new NextResponse(challenge, { status: 200 });
        } else {
            return new NextResponse('Forbidden', { status: 403 });
        }
    }
    return new NextResponse('Webhook is running properly! (GET)', { status: 200 });
}

export async function POST(req: NextRequest) {
    try {
        const body = await req.json();

        if (body.object) {
            if (
                body.entry &&
                body.entry[0].changes &&
                body.entry[0].changes[0] &&
                body.entry[0].changes[0].value.messages &&
                body.entry[0].changes[0].value.messages[0]
            ) {
                const phone_number_id = body.entry[0].changes[0].value.metadata.phone_number_id;
                const from = body.entry[0].changes[0].value.messages[0].from;
                const msg_body = body.entry[0].changes[0].value.messages[0].text?.body || '';

                if (msg_body) {
                    console.log(`Received WhatsApp message from ${from}: ${msg_body}`);
                    
                    // Initialize Embeddings & Vector Store
                    const embeddings = new GoogleGenerativeAIEmbeddings({
                        model: "gemini-embedding-2", 
                    });

                    // Retrieve top 5 matches via Supabase pgvector
                    const queryEmbedding = await embeddings.embedQuery(msg_body);
                    
                    const { data: topDocs, error } = await supabase.rpc('match_document_chunks', {
                        query_embedding: queryEmbedding,
                        match_threshold: 0.5,
                        match_count: 5
                    });
                    
                    if (error) {
                        console.error("Supabase Vector Search Error:", error);
                    }
                    const context = topDocs ? topDocs.map((doc: any) => doc.content).join("\n\n") : "";

                    // Initialize LLM
                    const llm = new ChatGoogleGenerativeAI({
                        model: "gemini-2.5-flash",
                        temperature: 0.1, // Near zero hallucination
                    });

                    // Construct WhatsApp-specific Prompt
                    const SYSTEM_TEMPLATE = `You are an elite Legal Assistant AI for "Get Legal Solution" (www.getlegalsolution.com) talking to a client on WhatsApp.
Your objective is to answer their query using the legal context provided below.

CORE RULES:
- First, attempt to answer the user's query strictly using the CONTEXT FROM VECTOR DB provided below. 
- If the CONTEXT is empty or does not contain the answer, you are authorized to use your general training knowledge (specifically regarding Pakistani Laws, Policies, and Legislation) to answer the user's query.
- When answering from general knowledge, add a brief disclaimer: *(Note: This answer is based on general legal knowledge and is not a substitute for formal advice from Get Legal Solution)*.
- Formatting: Format your response suitably for a WhatsApp message (use *bold* instead of HTML/Markdown tags, use newlines).
- Language: Reply in the language the user speaks.

CONTEXT FROM VECTOR DB:
{context}

USER MESSAGE:
{prompt}

Answer:`;

                    const promptTemplate = PromptTemplate.fromTemplate(SYSTEM_TEMPLATE);
                    const chain = promptTemplate.pipe(llm).pipe(new StringOutputParser());

                    // Await AI Response
                    const aiResponse = await chain.invoke({
                        context: context,
                        prompt: msg_body
                    });

                    console.log(`AI Response generated: ${aiResponse.substring(0, 50)}...`);

                    // Send AI Response back to WhatsApp
                    const WHATSAPP_TOKEN = process.env.WHATSAPP_API_TOKEN;
                    if (WHATSAPP_TOKEN) {
                        const fbResponse = await fetch(`https://graph.facebook.com/v20.0/${phone_number_id}/messages`, {
                            method: 'POST',
                            headers: { 
                                'Content-Type': 'application/json',
                                'Authorization': `Bearer ${WHATSAPP_TOKEN}`
                            },
                            body: JSON.stringify({
                                messaging_product: 'whatsapp',
                                to: from,
                                type: 'text',
                                text: { body: aiResponse }
                            })
                        });
                        
                        if (!fbResponse.ok) {
                            console.error("Meta API Error:", await fbResponse.text());
                        }
                    } else {
                        console.error("WHATSAPP_API_TOKEN is missing in environment variables!");
                    }
                }
            }
            return new NextResponse('EVENT_RECEIVED', { status: 200 });
        } else {
            return new NextResponse('Not Found', { status: 404 });
        }
    } catch (error: any) {
        console.error("Webhook Error:", error);
        return new NextResponse('Internal Server Error', { status: 500 });
    }
}
