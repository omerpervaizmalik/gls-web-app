export default async function handler(req, res) {
  const VERIFY_TOKEN = process.env.WHATSAPP_VERIFY_TOKEN || 'my_secure_verify_token_123';
  const WHATSAPP_TOKEN = process.env.WHATSAPP_API_TOKEN;

  if (req.method === 'GET') {
    const mode = req.query['hub.mode'];
    const token = req.query['hub.verify_token'];
    const challenge = req.query['hub.challenge'];

    if (mode === 'subscribe' && token === VERIFY_TOKEN) {
      console.log('Webhook verified successfully!');
      return res.status(200).send(challenge);
    } else {
      return res.status(403).send('Forbidden');
    }
  }

  if (req.method === 'POST') {
    try {
      const body = req.body;
      
      if (body.object) {
        if (
          body.entry &&
          body.entry[0].changes &&
          body.entry[0].changes[0] &&
          body.entry[0].changes[0].value.messages &&
          body.entry[0].changes[0].value.messages[0]
        ) {
          const phone_number_id = body.entry[0].changes[0].value.metadata.phone_number_id;
          const from = body.entry[0].changes[0].value.messages[0].from; // The user's phone number
          const msg_body = body.entry[0].changes[0].value.messages[0].text.body;

          console.log(`Received message from ${from}: ${msg_body}`);

          const responseText = "Hello! Our AI bot is currently being set up. We will reply to your message shortly.";
          
          if (WHATSAPP_TOKEN) {
            console.log("Sending reply with token...");
            const response = await fetch(`https://graph.facebook.com/v20.0/${phone_number_id}/messages`, {
              method: 'POST',
              headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${WHATSAPP_TOKEN}`
              },
              body: JSON.stringify({
                messaging_product: 'whatsapp',
                to: from,
                type: 'text',
                text: { body: responseText },
              }),
            });

            const data = await response.json();
            console.log("Meta API Response:", data);
          } else {
            console.error("ERROR: WHATSAPP_API_TOKEN is missing in environment variables!");
          }
        }
        return res.status(200).send('EVENT_RECEIVED');
      } else {
        return res.status(404).send('Not Found');
      }
    } catch (error) {
      console.error('Error handling webhook:', error);
      return res.status(500).send('Internal Server Error');
    }
  }

  return res.status(405).send('Method Not Allowed');
}
