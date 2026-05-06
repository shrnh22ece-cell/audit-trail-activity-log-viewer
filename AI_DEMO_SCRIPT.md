# AI Demo Script

## Goal
Demonstrate the AI service working end-to-end in the containerized environment using exact inputs and expected outputs.

## Setup
1. Start the full stack: `docker compose up --build`
2. Confirm services are running:
   - Backend: `http://localhost:8080`
   - AI Service: `http://localhost:5000`
   - Frontend: `http://localhost:5173`

## Demo Inputs and Expected Outputs

### 1. Summarization
**Input:**
```bash
curl -X POST http://localhost:5000/api/ai/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Summarize the benefits of electric vehicles in two sentences."}'
```
**Expected output:**
```json
{
  "prompt": "Summarize the benefits of electric vehicles in two sentences.",
  "response": "Electric vehicles reduce greenhouse gas emissions and lower fuel costs by using electricity instead of gasoline. They also improve air quality and require less maintenance due to fewer moving parts."
}
```

### 2. Explanation for non-technical audience
**Input:**
```bash
curl -X POST http://localhost:5000/api/ai/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Explain how JWT protects APIs in simple language."}'
```
**Expected output:**
```json
{
  "prompt": "Explain how JWT protects APIs in simple language.",
  "response": "JWT is a secure token that proves a user is allowed to access an API. When the user logs in, the system gives them a token, and each request includes that token so the API can verify the identity without sharing a password."
}
```

### 3. Practical security advice
**Input:**
```bash
curl -X POST http://localhost:5000/api/ai/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt":"List three best practices for creating strong passwords."}'
```
**Expected output:**
```json
{
  "prompt": "List three best practices for creating strong passwords.",
  "response": "Use a long passphrase with a mix of letters, numbers, and symbols; avoid common words and repeated patterns; and use a password manager to store unique passwords for each account."
}
```

### 4. Translation check
**Input:**
```bash
curl -X POST http://localhost:5000/api/ai/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Translate \"Hello\" to Spanish."}'
```
**Expected output:**
```json
{
  "prompt": "Translate \"Hello\" to Spanish.",
  "response": "Hola"
}
```

## 60-Second Technology Explanation for a Non-Technical Panel
Our demo shows a three-part system working together: a user-facing frontend, a secure Java backend, and an AI microservice. When a user sends a question, the frontend passes it to the AI service, which uses a prompt engine to generate a helpful answer and returns it as structured JSON. Behind the scenes, we protect the system with security checks, rate limiting, and token-based authentication so the AI service handles only valid requests and does not expose private information. This means the demo is not just about smart responses — it also shows a real-world architecture built for safety and reliability.
