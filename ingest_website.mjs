import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';
import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";
import dotenv from 'dotenv';

dotenv.config({ path: '.env.local' });

const WEBSITE_DIR = 'D:/Anti gravity/get-legal-solution';
const VECTOR_STORE_PATH = path.join(process.cwd(), 'vector_store.json');

async function ingest() {
    console.log("Starting website ingestion...");
    const files = fs.readdirSync(WEBSITE_DIR).filter(f => f.endsWith('.html'));
    
    let allText = "";

    for (const file of files) {
        if (file === '_navbar_snippet.html') continue; // Skip snippets

        const filePath = path.join(WEBSITE_DIR, file);
        const html = fs.readFileSync(filePath, 'utf-8');
        const $ = cheerio.load(html);

        // Remove script, style, nav, footer tags to get only main content
        $('script, style, nav, footer, header, .tidio-chat').remove();

        const title = $('title').text().trim() || path.parse(file).name;
        
        // Add a strong context prefix so the AI knows where this came from
        allText += `\n\n--- Source: Get Legal Solution Website - ${title} ---\n\n`;
        
        // Extract meaningful text, keeping basic paragraph spacing
        $('h1, h2, h3, h4, p, li').each((_, el) => {
            const text = $(el).text().trim();
            if (text.length > 20) {
                allText += text + "\n";
            }
        });
        
        console.log(`Parsed: ${file}`);
    }

    console.log(`Total extracted text length: ${allText.length} characters`);

    const paragraphs = allText.split(/\n\s*\n/);
    const chunks = [];
    let currentChunk = "";
    
    for (const p of paragraphs) {
        const trimmed = p.trim();
        if (!trimmed) continue;
        
        if (currentChunk.length + trimmed.length > 800) {
            chunks.push(currentChunk);
            currentChunk = trimmed + "\n\n";
        } else {
            currentChunk += trimmed + "\n\n";
        }
    }
    if (currentChunk.trim().length > 0) chunks.push(currentChunk);
    console.log(`Split into ${chunks.length} chunks.`);

    // Initialize Embeddings
    const embeddings = new GoogleGenerativeAIEmbeddings({
        model: "gemini-embedding-2",
        apiKey: process.env.GOOGLE_API_KEY
    });

    console.log("Generating embeddings (this may take a minute)...");
    
    const newDocs = [];
    for (let i = 0; i < chunks.length; i++) {
        const chunk = chunks[i];
        const embedding = await embeddings.embedQuery(chunk);
        
        newDocs.push({
            content: chunk,
            embedding: embedding,
            metadata: { source: "gls-website" }
        });
        
        if (i % 10 === 0) console.log(`Embedded ${i}/${chunks.length}`);
        
        // Prevent hitting rate limits
        await new Promise(r => setTimeout(r, 200)); 
    }

    // Load existing vector store
    let vectorDB = [];
    if (fs.existsSync(VECTOR_STORE_PATH)) {
        vectorDB = JSON.parse(fs.readFileSync(VECTOR_STORE_PATH, 'utf-8'));
    }

    const previousLength = vectorDB.length;
    
    // Check if we already added website data previously and clear it if so to avoid duplicates
    vectorDB = vectorDB.filter(doc => !doc.metadata || doc.metadata.source !== "gls-website");
    console.log(`Removed ${previousLength - vectorDB.length} old website chunks (if any).`);

    vectorDB.push(...newDocs);

    fs.writeFileSync(VECTOR_STORE_PATH, JSON.stringify(vectorDB, null, 2));
    console.log(`Successfully saved! Vector DB now has ${vectorDB.length} total entries.`);
}

ingest().catch(console.error);
