# Security Rules

## Bắt buộc cho mọi agent
- Không hardcode secret, credential, API key vào bất kỳ file nào.
- Chỉ commit .env.example (placeholder). .env trong .gitignore.
- Input validation bắt buộc ở server-side — không tin tưởng client.
- Parameterized query cho mọi DB operation — không string concatenation SQL.
- Authorization check: không chỉ "đã login" mà còn "có quyền với resource cụ thể".
- Không log: password, token, secret key, PII raw.
- Không trả về stack trace cho client.
- Rate limiting trên endpoints nhạy cảm (auth, payment, upload).
- CORS: whitelist domain cụ thể, không dùng *.

## CI/CD
- SAST scan (CodeQL/Semgrep) PASS trước khi merge.
- Container scan (Trivy): 0 Critical, 0 High → block build.
- Dependency audit: 0 Critical, 0 High CVE.
