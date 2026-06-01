import fs from 'fs';
import path from 'path';
import { Chroma } from "@langchain/community/vectorstores/chroma";
import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";
import { Document } from "@langchain/core/documents";
import Tesseract from 'tesseract.js';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const pdfParse = require('pdf-parse');
const mammoth = require('mammoth');

dotenv.config({ path: '.env.local' });

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const TEMPLATES_DIR = path.resolve(__dirname, '../../templates');
const VECTOR_STORE_PATH = path.resolve(__dirname, '../../vector_store.json');

// Initialize Embeddings
const embeddings = new GoogleGenerativeAIEmbeddings({
    model: "gemini-embedding-2", // Excellent for multilingual (Urdu/English)
});

// Hierarchical Chunking: We split by Markdown/Header sections if possible, then by paragraphs
const splitter = new RecursiveCharacterTextSplitter({
    chunkSize: 1000,
    chunkOverlap: 200,
    separators: ["\n## ", "\n### ", "\n\n", "\n", " ", ""],
});

async function parseDocument(filePath) {
    const ext = path.extname(filePath).toLowerCase();
    const dataBuffer = fs.readFileSync(filePath);
    
    if (ext === '.pdf') {
        const data = await pdfParse(dataBuffer);
        return data.text;
    } else if (ext === '.docx') {
        const result = await mammoth.extractRawText({ buffer: dataBuffer });
        return result.value;
    } else if (ext === '.txt' || ext === '.md') {
        return dataBuffer.toString('utf-8');
    } else if (ext === '.gif' || ext === '.png' || ext === '.jpg' || ext === '.jpeg') {
        console.log(`Running OCR on image: ${filePath}`);
        const { data: { text } } = await Tesseract.recognize(
            filePath,
            'eng+urd', // Support both English and Urdu OCR
            { logger: m => console.log(m) }
        );
        return text;
    }
    console.warn(`Unsupported file type: ${ext} for ${filePath}`);
    return null;
}

async function run() {
    console.log("Starting Ingestion Pipeline...");
    const files = fs.readdirSync(TEMPLATES_DIR);
    
    if (files.length === 0) {
        console.log("No templates found in the templates directory. Please add some templates.");
        return;
    }

    const docs = [];

    for (const file of files) {
        const filePath = path.join(TEMPLATES_DIR, file);
        if (fs.statSync(filePath).isDirectory()) continue;
        
        console.log(`Processing: ${file}`);
        const content = await parseDocument(filePath);
        
        if (!content) continue;

        // Basic metadata inference
        const isUrdu = /[\u0600-\u06FF]/.test(content); // Check for Arabic/Urdu script
        
        // You can enhance metadata extraction here (e.g., regex to find document type)
        let docType = "general";
        if (content.toLowerCase().includes("rental agreement")) docType = "rental_agreement";
        else if (content.toLowerCase().includes("petition")) docType = "petition";
        else if (content.toLowerCase().includes("deed")) docType = "deed";

        const doc = new Document({
            pageContent: content,
            metadata: {
                source: file,
                language: isUrdu ? "ur" : "en",
                document_type: docType
            }
        });
        docs.push(doc);
    }

    console.log(`Splitting ${docs.length} documents into chunks...`);
    const chunks = await splitter.splitDocuments(docs);
    
    console.log(`Adding ${chunks.length} chunks to Local JSON Vector Database...`);
    
    const chunkContents = chunks.map(c => c.pageContent);
    console.log("Generating embeddings...");
    const embeddedChunks = await embeddings.embedDocuments(chunkContents);
    
    const vectorDB = chunks.map((chunk, i) => ({
        content: chunk.pageContent,
        metadata: chunk.metadata,
        embedding: embeddedChunks[i]
    }));
    
    // Persist to file
    fs.writeFileSync(VECTOR_STORE_PATH, JSON.stringify(vectorDB));
    console.log(`Saved vector database to ${VECTOR_STORE_PATH}`);
    console.log("Ingestion Complete!");
}

run().catch(console.error);
