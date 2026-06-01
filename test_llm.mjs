import { GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI } from "@langchain/google-genai";
import { PromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';
dotenv.config({ path: '.env.local' });

async function test() {
    try {
        console.log("Invoking LLM gemini-2.5-pro...");
        const llm = new ChatGoogleGenerativeAI({
          model: "gemini-2.5-pro",
          temperature: 0.1,
        });

        const SYSTEM_TEMPLATE = `Just say 'Hello world'`;
        const promptTemplate = PromptTemplate.fromTemplate(SYSTEM_TEMPLATE);
        const chain = promptTemplate.pipe(llm).pipe(new StringOutputParser());

        const result = await chain.invoke({});
        console.log("Success! Output:", result);
    } catch (error) {
        console.error("Caught error:", error.message);
    }
}
test();
