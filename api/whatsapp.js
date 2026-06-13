export default async function handler(req, res) {
  const VERIFY_TOKEN = process.env.WHATSAPP_VERIFY_TOKEN || 'my_secure_verify_token_123';
  const WHATSAPP_TOKEN = process.env.WHATSAPP_API_TOKEN;

  // Debug endpoint
  if (req.method === 'GET' && req.query.debug === 'true') {
    return res.status(200).send(`Last Error: ${global.lastMetaError || 'None'}`);
  }

  if (req.method === 'GET') {
    const mode = req.query['hub.mode'];
    const token = req.query['hub.verify_token'];
    const challenge = req.query['hub.challenge'];

    if (mode && token) {
      if (mode === 'subscribe' && token === VERIFY_TOKEN) {
        return res.status(200).send(challenge);
      } else {
        return res.status(403).send('Forbidden');
      }
    }
    return res.status(200).send('Webhook is running properly! (GET)');
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
          const from = body.entry[0].changes[0].value.messages[0].from;
          const msg_body = body.entry[0].changes[0].value.messages[0].text?.body || '';

          if (WHATSAPP_TOKEN) {
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
                text: { body: 'Hello! Our AI bot is currently being set up. We will reply to your message shortly.' }
              })
            });
            
            if (!response.ok) {
              global.lastMetaError = await response.text();
              console.error("Meta API Error:", global.lastMetaError);
            } else {
              global.lastMetaError = "Success!";
            }
          } else {
            global.lastMetaError = "Token missing in environment";
          }
        }
        return res.status(200).send('EVENT_RECEIVED');
      } else {
        return res.status(404).send('Not Found');
      }
    } catch (error) {
      global.lastMetaError = error.message;
      return res.status(500).send('Internal Server Error');
    }
  }

  return res.status(405).send('Method Not Allowed');
}
