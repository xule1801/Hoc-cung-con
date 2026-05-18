# Testing Rules

- Unit coverage: ≥ 80% overall, ≥ 90% core services.
- CI FAIL BUILD nếu coverage dưới ngưỡng.
- Mọi Must-Have AC phải có E2E test.
- Test data: dùng builder pattern, không hardcode IDs, không dùng production data.
- Test phải độc lập (chạy được theo bất kỳ thứ tự nào) và deterministic.
- Mỗi bug fix phải có regression test: // Regression: BUG-[ID].
- 0 Critical CVE, 0 High CVE — CI fail nếu có.
- WCAG 2.1 AA — CI fail nếu có violation.
