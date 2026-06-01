import { NextRequest, NextResponse } from 'next/server';
import { GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import { createClient } from '@supabase/supabase-js';
import axios from 'axios';

// Initialize Supabase Client
const supabaseUrl = process.env.SUPABASE_URL || '';
const supabaseKey = process.env.SUPABASE_ANON_KEY || '';
const supabase = createClient(supabaseUrl, supabaseKey);

// Handle CORS Preflight
export async function OPTIONS() {
    return new NextResponse(null, {
        status: 200,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        },
    });
}

function cosineSimilarity(vecA: number[], vecB: number[]) {
    let dotProduct = 0, normA = 0, normB = 0;
    for (let i = 0; i < vecA.length; i++) {
        dotProduct += vecA[i] * vecB[i];
        normA += vecA[i] * vecA[i];
        normB += vecB[i] * vecB[i];
    }
    return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
}

// Helper to notify Admin via WhatsApp
async function notifyAdmin(sessionData: any, userMsg: string) {
    try {
        const adminPhone = "923014991700"; // Admin's WhatsApp number
        const token = process.env.WHATSAPP_TOKEN;
        const phoneId = process.env.WHATSAPP_PHONE_ID;
        
        if (!token || !phoneId) return;

        const userName = sessionData?.name || "Unknown User";
        const userPhone = sessionData?.phone || "No Phone provided";
        const sessionId = sessionData?.sessionId || "N/A";

        const textMessage = `🚨 *Human Expert Requested*\n\n*Name:* ${userName}\n*Phone:* ${userPhone}\n*Last Message:* "${userMsg}"\n\n*Chat ID:* ${sessionId}\n\nPlease review this lead and contact them.`;

        await axios.post(
            `https://graph.facebook.com/v20.0/${phoneId}/messages`,
            {
                messaging_product: "whatsapp",
                to: adminPhone,
                text: { body: textMessage },
            },
            {
                headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
            }
        );
        console.log("Admin notified via WhatsApp.");
    } catch (e) {
        console.error("Failed to notify admin via WhatsApp:", e);
    }
}

export async function POST(req: NextRequest) {
    try {
        const body = await req.json();
        const msg_body = body.message;
        const sessionId = body.sessionId || "unknown-session";
        const user = body.user || { name: 'Unknown', phone: 'Unknown' };

        if (!msg_body) {
            return NextResponse.json({ error: "Message is required" }, { status: 400 });
        }

        console.log(`Received WebChat message from ${user.name}: ${msg_body}`);

        // Log USER message to Supabase (non-blocking)
        supabase.from('chat_logs').insert([{
            session_id: sessionId,
            user_name: user.name,
            user_phone: user.phone,
            message: msg_body,
            sender: 'user'
        }]).then(({ error }) => { if (error) console.error("Supabase Log Error:", error) });
        
        // Initialize Embeddings & Vector Store
        const embeddings = new GoogleGenerativeAIEmbeddings({
            model: "gemini-embedding-2", 
        });

        // Load vector store via static import
        const vectorDB = require('../../../../vector_store.json');

        // Retrieve top 5 matches
        const queryEmbedding = await embeddings.embedQuery(msg_body);
        const scoredDocs = vectorDB.map((doc: any) => ({
            ...doc,
            score: cosineSimilarity(queryEmbedding, doc.embedding)
        }));
        
        scoredDocs.sort((a: any, b: any) => b.score - a.score);
        const topDocs = scoredDocs.slice(0, 5);
        const context = topDocs.map((doc: any) => doc.content).join("\n\n");

        // Check if user is requesting a human
        const isHumanRequest = msg_body.toLowerCase().includes("human") || 
                               msg_body.toLowerCase().includes("talk to someone") || 
                               msg_body.toLowerCase().includes("expert") ||
                               msg_body.toLowerCase().includes("call me");

        let aiResponse = "";

        if (isHumanRequest) {
            aiResponse = `I have notified our legal experts. Someone from Get Legal Solution will contact you shortly at ${user.phone}.`;
            // Trigger Admin WhatsApp Alert
            await notifyAdmin({ name: user.name, phone: user.phone, sessionId }, msg_body);
        } else {
            // Initialize LLM
            const llm = new ChatGoogleGenerativeAI({
                model: "gemini-2.5-flash",
                temperature: 0.1, 
            });

            // Construct Webchat-specific Prompt
            const SYSTEM_TEMPLATE = `You are an elite Legal Assistant AI for "Get Legal Solution" (www.getlegalsolution.com) talking to a client on their website chat.
Your objective is to answer their query using the legal context provided below.

CORE RULES:
- First, attempt to answer the user's query strictly using the CONTEXT FROM VECTOR DB provided below. 
- If the CONTEXT is empty or does not contain the answer, you are authorized to use your general training knowledge (specifically regarding Pakistani Laws, Policies, and Legislation) to answer the user's query.
- When answering from general knowledge, add a brief disclaimer: *(Note: This answer is based on general legal knowledge and is not a substitute for formal advice from Get Legal Solution)*.
- Formatting: Format your response beautifully for a modern web chat interface. You can use standard Markdown (bold, italics, bullet points).
- If the user explicitly asks for a human, say you will connect them.
- Keep your answers concise, professional, and helpful.

CONTEXT FROM VECTOR DB:
{context}

USER MESSAGE:
{prompt}

Answer:`;

            const promptTemplate = PromptTemplate.fromTemplate(SYSTEM_TEMPLATE);
            const chain = promptTemplate.pipe(llm).pipe(new StringOutputParser());

            // Await AI Response
            aiResponse = await chain.invoke({
                context: context,
                prompt: msg_body
            });
            
            // Just in case the AI generated a human handoff message itself
            if (aiResponse.toLowerCase().includes("will connect you") || aiResponse.toLowerCase().includes("will contact you")) {
                await notifyAdmin({ name: user.name, phone: user.phone, sessionId }, msg_body);
            }
        }

        console.log(`AI Response generated: ${aiResponse.substring(0, 50)}...`);

        // Log AI response to Supabase (non-blocking)
        supabase.from('chat_logs').insert([{
            session_id: sessionId,
            user_name: user.name,
            user_phone: user.phone,
            message: aiResponse,
            sender: 'bot'
        }]).then(({ error }) => { if (error) console.error("Supabase Log Error:", error) });

        return NextResponse.json({ response: aiResponse }, {
            status: 200,
            headers: {
                'Access-Control-Allow-Origin': '*', 
            }
        });
    } catch (error: any) {
        console.error("WebChat Error:", error);
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500, headers: { 'Access-Control-Allow-Origin': '*' } });
    }
}
