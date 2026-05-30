// In a real production app, you should use a database (e.g., Neon Postgres) to store user states.
// For demonstration, we use a simple in-memory object. Note: This will reset on Vercel cold starts.
const userStates = {};

export async function generateWhatsAppResponse(message, phoneNumber) {
  // Check if user is already in 'human' mode
  if (userStates[phoneNumber] === 'human_intervention') {
    // We ignore messages from this user, as a human is expected to reply via Meta Business Suite
    console.log(`Ignoring message from ${phoneNumber} (human intervention active)`);
    return null;
  }

  const lowercaseMsg = message.toLowerCase();

  // Detect Fallback Intent
  if (
    lowercaseMsg.includes('human') || 
    lowercaseMsg.includes('agent') || 
    lowercaseMsg.includes('support') ||
    lowercaseMsg.includes('representative') ||
    lowercaseMsg.includes('call')
  ) {
    userStates[phoneNumber] = 'human_intervention';
    return "I am handing this over to our legal team. A human representative will review your query and reply shortly.";
  }

  // --- RAG MODULE INTEGRATION ---
  // Here, we would ideally make a fetch request to your gls-rag-module API,
  // or use the LangChain logic directly if migrated to gls-web-app.
  
  // Example of calling the gls-rag-module API (assuming it's running locally or deployed):
  /*
  try {
    const response = await fetch('https://your-rag-module-url.com/api/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: message })
    });
    const data = await response.json();
    return data.answer;
  } catch (error) {
    console.error("RAG Error:", error);
    return "I'm having trouble connecting to the legal database right now. Please try again later.";
  }
  */

  // Placeholder AI response for now
  return `(AI Bot): Thank you for your question regarding Pakistani law. I am currently being connected to the Legal Knowledge Base. You asked: "${message}"`;
}
