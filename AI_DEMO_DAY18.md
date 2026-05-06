# Day 18 Demo: AI Recommend & Generate Report

## Demo Overview
This demo exercises the AI service with two key flows:
1. AI Recommendation
2. Generate Report

It also confirms the service health endpoints work correctly.

## 1. AI Recommend
**Input:**
```bash
curl -X POST http://localhost:5000/api/ai/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Recommend three ways an enterprise can improve security for its AI pipeline."}'
```
**Expected output:**
```json
{
  "prompt": "Recommend three ways an enterprise can improve security for its AI pipeline.",
  "response": "1. Enforce strong identity and access controls using tokens like JWT for each service. 2. Validate and sanitize prompts before they reach the AI model to block injection attempts. 3. Apply rate limiting and security headers to protect the API and prevent abuse."
}
```

## 2. Generate Report
**Input:**
```bash
curl -X POST http://localhost:5000/api/ai/prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Generate a short report summary on improving cloud security posture."}'
```
**Expected output:**
```json
{
  "prompt": "Generate a short report summary on improving cloud security posture.",
  "response": "Improving cloud security posture requires strong identity controls, secure configuration management, and continuous monitoring. Teams should ensure encrypted communications, enforce least privilege access, and regularly audit cloud resources to reduce risk."
}
```

## 3. Health Checks
Confirm the backend and AI service are running.

**Backend health:**
```bash
curl http://localhost:8080/api/health
```
Expected output:
```json
{"status": "ok"}
```

**AI service health:**
```bash
curl http://localhost:5000/health
```
Expected output:
```json
{"status": "ok"}
```

## 60-Second Explanation: Flask + Groq
The AI service is a simple Flask app that receives user prompts and forwards them to a Groq-compatible model API. Flask handles HTTP requests, sanitizes the prompt for safety, and returns the model's response as JSON. Groq is the external AI engine that generates the text based on our prompt instructions. Together, Flask manages the service logic and security, while Groq provides the actual language intelligence.
