# Hoc-cung-con

> Khởi tạo: 2026-05-18 21:44

## Quickstart

```bash
cp .env.example .env   # Điền các giá trị cần thiết
docker-compose up -d   # Start services
npm run db:migrate     # Chạy migrations
npm run dev            # Start development server
```

## Multi-Agent Workflow

Dự án này sử dụng Antigravity multi-agent workflow với 8 gate:

```
Gate 0 — Project Init     [workflow-controller]
Gate 1 — BA Analysis      [ba-agent]
Gate 2 — Architecture     [architect-agent + ba-agent validate]
Gate 3 — Development      [dev-agent]
Gate 4 — Testing          [test-agent]
Gate 5 — Code Review      [review-agent]
Gate 6 — Release Prep     [devops-agent]
Gate 7 — Deploy           [devops-agent + User Approval]
Gate 8 — Post-Deploy      [devops-agent]
```

Xem docs/workflow-status.md để theo dõi tiến độ.

## Cấu trúc

```
.agent/skills/    ← Agent definitions
.agent/rules/     ← Coding/security/testing rules
.agent/workflows/ ← Hotfix, change request workflows
docs/             ← Tài liệu workflow (01 → 10)
src/              ← Source code
tests/            ← Test files (unit/integration/e2e/performance)
infra/            ← Infrastructure as Code (Terraform)
.github/workflows ← CI/CD pipelines
```
