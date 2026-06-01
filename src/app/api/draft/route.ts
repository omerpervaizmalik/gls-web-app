import { NextRequest, NextResponse } from 'next/server';
import { GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import fs from 'fs';
import path from 'path';

function cosineSimilarity(vecA: number[], vecB: number[]) {
    let dotProduct = 0, normA = 0, normB = 0;
    for (let i = 0; i < vecA.length; i++) {
        dotProduct += vecA[i] * vecB[i];
        normA += vecA[i] * vecA[i];
        normB += vecB[i] * vecB[i];
    }
    return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { documentType, prompt } = body;
    const userPrompt = prompt || documentType;

    // Initialize Embeddings & Vector Store
    const embeddings = new GoogleGenerativeAIEmbeddings({
        model: "gemini-embedding-2", 
    });

    // Load from disk
    const storePath = path.resolve(process.cwd(), 'vector_store.json');
    let vectorDB: any[] = [];
    if (fs.existsSync(storePath)) {
        const data = fs.readFileSync(storePath, 'utf8');
        vectorDB = JSON.parse(data);
    }
    
    // Retrieve top 5 matches
    const queryEmbedding = await embeddings.embedQuery(userPrompt);
    const scoredDocs = vectorDB
        .map(doc => ({
            ...doc,
            score: cosineSimilarity(queryEmbedding, doc.embedding)
        }));
    
    scoredDocs.sort((a: any, b: any) => b.score - a.score);
    const topDocs = scoredDocs.slice(0, 5);
    
    const context = topDocs.map(doc => doc.content).join("\n\n");

        const llm = new ChatGoogleGenerativeAI({
          model: "gemini-2.5-flash",
          temperature: 0.1, // Near zero hallucination
        });

    // Removed Step 1 Summary Phase completely based on user request
    const SYSTEM_TEMPLATE = `ROLE & CONTEXT
You are an elite AI Legal Engineer and an advanced Retrieval-Augmented Generation (RAG) Architect specializing in Jurisprudence and Legal Tech automation. Your objective is to power the AI Agent for "Get Legal Solution" (www.getlegalsolution.com). 

Your primary task is to help users dynamically draft precise, legally binding documents by retrieving strict context from the firm's vetted, pre-chunked vector database templates and merging them with user-submitted credentials and case variables.

SYSTEM CONSTRAINTS & CORE RULES
A. ABSOLUTE ZERO HALLUCINATION (The Core Directive)
- You must strictly use the clauses, terminology, and structures provided in the retrieved vector context. Do not invent legal statutes, laws, or precedents.
- If the retrieved context does not contain a specific requested clause, explicitly state: "The system requires specific template updates to include this clause. Please contact Get Legal Solution administration."

B. STRUCTURAL INTEGRITY & FORMATTING (HTML)
- You MUST output the drafted document in clean HTML format. Use '<h1 style="text-align: center;">' for titles, '<h2>' for subtitles, '<p>' for paragraphs, '<strong>' for bolding names and important clauses, and '<ul>'/'<li>' for lists.
- Do NOT wrap the output in markdown code blocks (\`\`\`html). Output raw HTML directly.
- All generated documents must follow professional legal formatting:
  - Clear titles in uppercase.
  - Numbered paragraphs for clauses.
  - Clearly demarcated execution and witness blocks at the bottom.
  - "Jurisdiction" and "Governing Law" clauses must be explicitly included based on the template.

C. LANGUAGE SUPPORT
- Maintain the language (English or Urdu) as dictated by the template context.

CONTEXT FROM VECTOR DB:
{context}

USER REQUIREMENTS / PROMPT:
{prompt}

Draft the legal document by flawlessly merging the context with the user requirements. Do NOT invent anything outside the context.`;

    const promptTemplate = PromptTemplate.fromTemplate(SYSTEM_TEMPLATE);
    
    const chain = promptTemplate.pipe(llm).pipe(new StringOutputParser());

    const result = await chain.invoke({
        context: context,
        prompt: userPrompt
    });

    return NextResponse.json({ result });

  } catch (error) {
    console.error(error);
    return NextResponse.json({ error: "Failed to generate document" }, { status: 500 });
  }
}
