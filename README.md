# Internship Tool Project

This repository includes a full-stack intern project scaffold with:

- `backend/` - Spring Boot REST microservice
- `ai-service/` - Flask-based AI microservice
- `frontend/` - React + Vite frontend
- `docker-compose.yml` - Local multi-service development setup

## Structure

- `backend/`
  - `src/main/java/com/internship/tool/`
  - `src/main/resources/db/migration/`
  - `pom.xml`

- `ai-service/`
  - `routes/`
  - `services/`
  - `prompts/`
  - `app.py`
  - `requirements.txt`

- `frontend/`
  - `src/components/`
  - `src/pages/`
  - `src/`
  - `package.json`

## Run locally

1. Configure environment variables:
   - Copy `.env.example` to `.env` and set `OPENAI_API_KEY`
2. Start backend:
   - `cd backend && ./mvnw spring-boot:run`
3. Start AI service:
   - `cd ai-service && python -m pip install -r requirements.txt && python app.py`
4. Start frontend:
   - `cd frontend && npm install && npm run dev`
5. Use `docker-compose up --build` for containerized development.
