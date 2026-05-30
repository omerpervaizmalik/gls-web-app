import { NextResponse } from 'next/server';
import { generateWhatsAppResponse } from '@/lib/aiChat';

const VERIFY_TOKEN = process.env.WHATSAPP_VERIFY_TOKEN || 'my_secure_verify_token_123';
const WHATSAPP_TOKEN = process.env.WHATSAPP_API_TOKEN;

// Meta Webhook Verification
export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const mode = searchParams.get('hub.mode');
  const token = searchParams.get('hub.verify_token');
  const challenge = searchParams.get('hub.challenge');

  if (mode === 'subscribe' && token === VERIFY_TOKEN) {
    console.log('Webhook verified successfully!');
    return new NextResponse(challenge, { status: 200 });
  } else {
    return new NextResponse('Forbidden', { status: 403 });
  }
}

// Handle Incoming WhatsApp Messages
export async function POST(request) {
  try {
    const body = await request.json();

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

        // Generate AI Response or Human Fallback
        const aiResponse = await generateWhatsAppResponse(msg_body, from);

        // Send reply via Meta API
        if (aiResponse) {
          await fetch(`https://graph.facebook.com/v17.0/${phone_number_id}/messages?access_token=${WHATSAPP_TOKEN}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              messaging_product: 'whatsapp',
              to: from,
              text: { body: aiResponse },
            }),
          });
        }
      }
      return new NextResponse('EVENT_RECEIVED', { status: 200 });
    } else {
      return new NextResponse('Not Found', { status: 404 });
    }
  } catch (error) {
    console.error('Error handling webhook:', error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
