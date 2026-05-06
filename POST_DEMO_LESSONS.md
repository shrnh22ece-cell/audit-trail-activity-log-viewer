# Post-Demo Lessons Learned

## Lessons Learned
- **Containerization matters**: The demo showed how Docker Compose is essential for a reproducible environment, but it also highlighted the need for a full frontend container build and runtime validation.
- **Prompt engineering is key**: Small prompt format improvements dramatically improved AI response quality, especially when guiding the model with a system prompt.
- **Security is integral, not optional**: Adding JWT authentication, rate limiting, injection protections, and security headers made the system much stronger and more demonstration-ready.
- **Documentation adds confidence**: Having clear demo scripts, summary cards, and talking points made the presentation smoother and easier for non-technical audiences.

## Features for Future Sprints
- Add production-grade user management and persistent authentication storage.
- Implement a proper backend database for real data instead of in-memory H2.
- Add automated CI/CD security scanning and dependency auditing.
- Enhance frontend UI to showcase AI prompts and results in a polished dashboard.
- Add logging and observability for the AI service and backend request flows.
- Build a more robust retry and fallback strategy for Groq API failures.

## Feedback for Mentor
- The sprint process worked well with daily milestones and clear deliverables.
- The project benefits from more structured testing around containerized E2E scenarios and security validation.
- It would be helpful to include an additional review step for privacy and PII compliance before demo day.
- The mentor guidance enabled rapid progress across backend, AI, and security areas.

## Notes
- This document captures the post-demo retrospective and should be used to inform planning for the next phase.
