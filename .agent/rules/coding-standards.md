# Coding Standards

- TypeScript strict mode bắt buộc. Không dùng `any`.
- Function: ≤ 20 dòng, ≤ 3 tham số, không lồng if/else quá 3 cấp.
- Naming: camelCase (vars), PascalCase (classes), UPPER_SNAKE_CASE (constants),
  kebab-case (files TS/JS), PascalCase (React components).
- DB: snake_case bảng (plural), snake_case columns.
- Commit: Conventional Commits — feat/fix/docs/test/chore/perf/security.
- Không nuốt lỗi im lặng. Không hardcode secret. Không console.log ở production.
- JSDoc bắt buộc cho public functions và complex business logic.
