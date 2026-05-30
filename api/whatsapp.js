export default async function handler(req, res) {
  const VERIFY_TOKEN = process.env.WHATSAPP_VERIFY_TOKEN || 'my_secure_verify_token_123';
  const WHATSAPP_TOKEN = process.env.WHATSAPP_API_TOKEN;

  // Handle Meta Verification (GET Request)
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

  // Handle Incoming WhatsApp Messages (POST Request)
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
          const from = body.entry[0].changes[0].value.messages[0].from;
          const msg_body = body.entry[0].changes[0].value.messages[0].text.body;

          console.log(`Received message from ${from}: ${msg_body}`);

          const responseText = "Hello! Our AI bot is currently being set up. We will reply to your message shortly.";
          
          if (WHATSAPP_TOKEN) {
            await fetch(`https://graph.facebook.com/v17.0/${phone_number_id}/messages?access_token=${WHATSAPP_TOKEN}`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                messaging_product: 'whatsapp',
                to: from,
                text: { body: responseText },
              }),
            });
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
