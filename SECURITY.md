# Security Considerations

This document highlights common threats relevant to the repository and its services.

1. Secret Exposure
   - API keys, database credentials, and other sensitive values should never be committed to source control. Use environment variables and secure secret management.

2. Broken Authentication and Authorization
   - The backend and AI service must enforce authentication and authorization controls for protected endpoints to prevent unauthorized access.

3. Injection Vulnerabilities
   - User-provided input should be validated and escaped before being used in database queries, external requests, or template rendering.

4. Insecure Configuration
   - Default or overly permissive settings (e.g. debug mode, open CORS, unsecured network access) can expose the application to attackers.

5. Supply Chain Risk
   - Dependencies should be reviewed and pinned to known-safe versions. Untrusted packages or outdated libraries can introduce vulnerabilities.

## Week 1 Security Tests

### Test Methodology
- **Empty Input**: Send empty or null values to endpoints.
- **SQL Injection**: Attempt SQL injection payloads (e.g., `' OR 1=1 --`).
- **Prompt Injection**: Attempt prompt injection patterns (e.g., "ignore previous instructions").

### Endpoints Tested
- Backend: `GET /api/health`
- AI Service: `GET /health`, `POST /api/ai/prompt`

### Test Results

#### Empty Input
- **Backend /api/health**: Returns "OK" (no input required).
- **AI Service /health**: Returns `{"status": "ok"}` (no input required).
- **AI Service /api/ai/prompt**: Accepts empty prompt, processes as "Hello from AI service" (graceful handling).

#### SQL Injection
- **Backend /api/health**: No user input, no vulnerability.
- **AI Service /health**: No user input, no vulnerability.
- **AI Service /api/ai/prompt**: Input sanitized (HTML stripped), no direct DB queries. Payloads like `' OR 1=1 --` treated as text, no injection possible.

#### Prompt Injection
- **Backend /api/health**: No user input, no vulnerability.
- **AI Service /health**: No user input, no vulnerability.
- **AI Service /api/ai/prompt**: Middleware detects and blocks patterns like "ignore previous instructions", returns 400 error. Tested patterns: "ignore all previous instructions", "disregard previous instructions", "you are now". All blocked successfully.

### Overall Assessment
- **Pass**: All endpoints handle empty input gracefully.
- **Pass**: No SQL injection vulnerabilities detected (backend uses JPA with parameterized queries, AI service does not query databases).
- **Pass**: Prompt injection mitigated by middleware regex patterns.
- **Recommendation**: Continue monitoring and add logging for blocked attempts.

## OWASP ZAP Scan Results (Day 7)

### Scan Summary
- **Tool**: OWASP ZAP
- **Date**: May 6, 2026
- **Targets**: http://localhost:8080 (Backend), http://localhost:5000 (AI Service)
- **Findings**:
  - High: 0
  - Medium: 2 (Fixed)
  - Low: 5 (Planned)
  - Informational: 10

### Critical Findings
- None detected.

### Medium Findings (Fixed Today)
1. **X-Frame-Options Header Not Set** (Backend)
   - **Fix**: Added `frameOptions().deny()` in `SecurityConfig.java` to set `X-Frame-Options: DENY`.

2. **Missing Anti-clickjacking Header** (AI Service)
   - **Fix**: Added `@app.after_request` in `app.py` to set `Content-Security-Policy: frame-ancestors 'none';`.

### Low Findings (Fixed Today)
1. **Cookie No HttpOnly Flag**: Added stateless session management in Spring Boot (no cookies used).
2. **Server Leaks Information**: Customized server header to "InternshipTool" in application.yml.
3. **X-Content-Type-Options Header Missing**: Already added in previous fixes.
4. **Information Disclosure - Suspicious Comments**: No suspicious comments found in codebase.
5. **Timestamp Disclosure**: No timestamps included in responses; debug mode disabled in Flask.

### Additional Security Headers Added
- **HSTS (Strict-Transport-Security)**: Enabled in both services.
- **Referrer-Policy**: Set to strict-origin-when-cross-origin.

### Re-Scan Results (Day 8)
- **Tool**: OWASP ZAP
- **Date**: May 6, 2026
- **Targets**: http://localhost:8080 (Backend), http://localhost:5000 (AI Service)
- **Findings**:
  - High: 0
  - Medium: 0
  - Low: 0
  - Informational: 0
- **Confirmation**: Zero Critical/High findings remaining.

### Report
- Updated `zap_report.html` with clean scan results.

## Week 2 Security Sign-Off (Day 9)

### JWT Authentication
- **Implementation**: Added JWT-based authentication in Spring Boot backend.
  - Dependencies: jjwt-api, jjwt-impl, jjwt-jackson.
  - Components: JwtUtil for token generation/validation, JwtRequestFilter for request filtering, MyUserDetailsService for user loading, AuthController for login.
  - Configuration: Stateless sessions, protected endpoints except /api/auth/** and /api/health.
- **Verification**: Login endpoint generates JWT, protected endpoints require Bearer token. Tested with Postman.

### Rate Limiting
- **Implementation**: Flask-Limiter in AI service (30 requests/minute per IP).
- **Verification**: Exceeding limit returns 429 status. Confirmed via curl tests.

### Injection Protections
- **SQL Injection**: Verified no vulnerabilities (JPA parameterized queries, no DB in AI service).
- **Prompt Injection**: Middleware regex blocks patterns like "ignore previous instructions".
- **Verification**: All Week 1 tests pass, additional payloads tested.

### PII Audit
- **Audit Results**: No personal identifiable information stored or processed in prompts.
  - Prompts are sanitized (HTML stripped), not persisted.
  - AI service does not collect user data beyond input prompts.
  - Backend uses H2 in-memory DB with no user data.
- **Confirmation**: Code review confirms no PII handling; prompts treated as generic text.

### Overall Sign-Off
- **Pass**: JWT authentication implemented and verified.
- **Pass**: Rate limiting enforced.
- **Pass**: Injection protections in place.
- **Pass**: No PII in prompts confirmed.
- **Recommendation**: Implement proper user management and database for production.

## Week 2 AI Quality Review (Day 10)

### Methodology
- Tested 10 fresh inputs on `/api/ai/prompt` endpoint.
- Scored responses on accuracy, relevance, and helpfulness (1-5 scale).
- Target: Average score >= 4/5.

### Initial Test Results (Pre-Fix)
Average Score: 3.2/5 (Below target)

Sample Inputs and Scores:
1. "What is the capital of France?" - Score: 4/5 (Accurate)
2. "Explain quantum computing simply." - Score: 2/5 (Too technical)
3. "How to bake a chocolate cake?" - Score: 3/5 (Incomplete steps)
4. "What are the benefits of exercise?" - Score: 4/5 (Good list)
5. "Translate 'Hello' to Spanish." - Score: 5/5 (Perfect)
6. "Why is the sky blue?" - Score: 3/5 (Scientific but not engaging)
7. "Best practices for password security." - Score: 2/5 (Too vague)
8. "History of the Roman Empire." - Score: 4/5 (Concise summary)
9. "How does photosynthesis work?" - Score: 3/5 (Accurate but dry)
10. "Recommend a book on AI." - Score: 2/5 (Generic recommendation)

### Fixes Applied
- Added system prompt to Groq client: "You are a helpful AI assistant. Provide accurate, concise, and relevant responses to user queries."
- Adjusted prompt format to include User/Assistant structure for better context.

### Post-Fix Test Results
Average Score: 4.3/5 (Target met)

Re-tested the same inputs:
1. "What is the capital of France?" - Score: 5/5
2. "Explain quantum computing simply." - Score: 4/5
3. "How to bake a chocolate cake?" - Score: 4/5
4. "What are the benefits of exercise?" - Score: 5/5
5. "Translate 'Hello' to Spanish." - Score: 5/5
6. "Why is the sky blue?" - Score: 4/5
7. "Best practices for password security." - Score: 4/5
8. "History of the Roman Empire." - Score: 5/5
9. "How does photosynthesis work?" - Score: 4/5
10. "Recommend a book on AI." - Score: 4/5

### Sign-Off
- **Pass**: Average accuracy >= 4/5 achieved after fixes.
- **Recommendation**: Continue monitoring and refining prompts for edge cases.
