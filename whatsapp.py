from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

# Configure your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # Get the incoming WhatsApp message
    incoming_msg = request.values.get('Body', '').strip()
    
    # Generate a response using OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=incoming_msg,
        max_tokens=150
    )
    
    # Get the text from OpenAI's response
    ai_response = response.choices[0].text.strip()
    
    # Create a response to send back to WhatsApp
    resp = MessagingResponse()
    resp.message(ai_response)
    
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
