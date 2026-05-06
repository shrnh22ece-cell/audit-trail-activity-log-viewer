# AI Project Summary Card — Copy 2

## Key Endpoints
1. **AI Prompt Service**
   - `POST /api/ai/prompt`
   - Sends a user prompt to the AI microservice and returns a JSON response.

2. **Backend Health Check**
   - `GET /api/health`
   - Confirms the Spring Boot backend is running and available.

3. **AI Service Health Check**
   - `GET /health`
   - Confirms the Flask AI microservice is running and available.

## Technology Stack
- **Frontend**: React + Vite
- **Backend**: Spring Boot (Java 17)
- **AI Service**: Flask (Python 3.12)
- **AI Integration**: Groq-compatible prompt engine with secure prompt handling
- **Security**: JWT auth, rate limiting, prompt injection filtering, security headers
- **Deployment**: Docker Compose multi-service setup

## GitHub Link
https://github.com/shrnh22ece-cell/audit-trail-activity-log-viewer

## Demo Day Notes
- This card summarizes the full stack and AI workflow in one page.
- Use it as a quick reference when presenting live or answering questions.
