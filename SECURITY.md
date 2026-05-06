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

### Low Findings (Planned Fixes)
1. **Cookie No HttpOnly Flag**: Set HttpOnly on session cookies.
2. **Server Leaks Information**: Customize server header in Spring Boot.
3. **X-Content-Type-Options Header Missing**: Already added in fixes above.
4. **Information Disclosure - Suspicious Comments**: Review and remove debug comments.
5. **Timestamp Disclosure**: Remove timestamps from error responses.

### Report
- Exported to `zap_report.html`.
