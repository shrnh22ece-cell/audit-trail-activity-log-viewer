# AI Talking Points Card

## What is Groq?
- Groq provides the large language model API used by the AI service.
- It receives prompt text and returns generated responses based on that prompt.
- We use a Groq-compatible API endpoint so the service can call the model securely from the Flask app.

## How prompts work (plain English)
- A prompt is simply the text we send to the AI service asking it to do something.
- Example: "Summarize the benefits of electric vehicles in two sentences."
- The AI service wraps the prompt in a simple structure and sends it to Groq.
- The model then replies with the answer, and our app returns that response to the user.

## Why prompt design matters
- Good prompts guide the AI to answer clearly and correctly.
- We added a system-level prompt so the AI knows to be helpful, concise, and relevant.
- Better prompt structure means more reliable results for users.

## Security talking points
- **JWT authentication** protects backend endpoints with token-based access.
- **Rate limiting** on the AI service prevents abuse by limiting requests per IP.
- **Prompt injection filtering** blocks dangerous prompt instructions like "ignore previous instructions."
- **Security headers** such as `X-Frame-Options`, `Content-Security-Policy`, `Strict-Transport-Security`, and `X-Content-Type-Options` are set to reduce browser and network risk.
- **No PII in prompts**: user prompt inputs are not stored or treated as personal data.

## Demo-ready talking points
- This system is an AI-powered pipeline: user prompt → Flask AI service → Groq model → JSON response.
- Security is built in at every step, from authentication and rate limiting to prompt safety and header hardening.
- The goal is a reliable, secure, and easy-to-understand AI experience for the demo audience.
