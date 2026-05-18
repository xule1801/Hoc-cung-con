# Quy tắc làm việc — Antigravity Multi-Agent Workflow

## 1. Triết lý dự án

- Luôn chọn giải pháp **TỐT NHẤT phù hợp với bài toán** — không dừng ở
  mức tối thiểu, nhưng cũng không over-engineer khi không cần thiết.
- Giao diện người dùng phải **HIỆN ĐẠI, nhất quán và accessible** — yêu cầu bắt buộc.
- Ưu tiên theo thứ tự: bảo mật → hiệu năng → khả năng mở rộng → UX.
- Mọi quyết định kỹ thuật quan trọng phải có lý do được ghi lại (ADR).

---

## 2. Nguyên tắc bất biến

Áp dụng cho **mọi agent**, không có ngoại lệ:

1. Không viết code khi chưa có docs/02-ba-analysis.md và
   docs/05-ba-architecture-validation.md với kết luận PASS.
2. Luôn tạo hoặc cập nhật tài liệu trong `docs/` trước khi code.
3. Mọi tính năng phải có Acceptance Criteria và test case tương ứng.
4. Unit test coverage **bắt buộc ≥ 80%** — CI fail build nếu dưới ngưỡng.
5. Không tự deploy production khi chưa có xác nhận rõ ràng của người dùng.
6. Không tự commit khi chưa có xác nhận của người dùng.
7. Không hardcode secret, credential, API key vào bất kỳ file nào.
8. Không bỏ qua bất kỳ gate nào — kể cả khi người dùng yêu cầu
   (phải cảnh báo rủi ro và ghi nhận vào docs/workflow-status.md).
9. Không tự ý đơn giản hóa thiết kế so với docs/04-architecture.md đã duyệt.
10. Không xóa dữ liệu bất kỳ môi trường nào khi chưa có xác nhận.

---

## 3. Trạng thái Gate

| Trạng thái              | Ý nghĩa                                              |
|------------------------|------------------------------------------------------|
| `IN_PROGRESS`           | Agent đang thực hiện                                 |
| `PASS`                  | Đạt yêu cầu, được chuyển gate                       |
| `PASS_WITH_MINOR_ISSUES`| Đạt yêu cầu, có điểm nhỏ cần cải thiện (không block)|
| `NEED_REVISION`         | Chưa đạt, có Major issue — quay lại agent tạo output |
| `FAIL`                  | Có Blocker issue — dừng luồng, escalate người dùng   |
| `BLOCKED`               | Thiếu thông tin/điều kiện — ghi rõ, chờ bổ sung     |
| `WAITING_USER_APPROVAL` | Cần người dùng xác nhận trước khi thực hiện          |

---

## 4. Quy trình 8 Gate

```
Gate 0 — Project Init         [workflow-controller]
Gate 1 — BA Analysis          [ba-agent]
Gate 2 — Architecture         [architect-agent] ← BA review
Gate 3 — Development          [dev-agent]
Gate 4 — Testing              [test-agent]
Gate 5 — Code Review          [review-agent]
Gate 6 — Release Preparation  [devops-agent]
Gate 7 — Deploy               [devops-agent] ← User approval bắt buộc
Gate 8 — Post-Deploy Monitor  [devops-agent]
```

Retry limit:
- Test FAIL (Gate 4): tối đa 3 lần → escalate
- Review NEED_REVISION (Gate 5): tối đa 2 lần → escalate
- Build FAIL (Gate 6): tối đa 2 lần → escalate

---

## 5. Cấu trúc tài liệu bắt buộc

```
docs/
├── 01-project-charter.md          ← Gate 0
├── 02-ba-analysis.md              ← Gate 1
├── 03-requirement-review.md       ← Gate 1
├── 04-architecture.md             ← Gate 2
├── 04-adr.md                      ← Gate 2 (Architecture Decision Records)
├── 05-ba-architecture-validation.md ← Gate 2
├── 06-dev-notes.md                ← Gate 3
├── 07-test-report.md              ← Gate 4
├── 08-code-review.md              ← Gate 5
├── 09-release-report.md           ← Gate 6
├── 10-post-deploy-report.md       ← Gate 8
├── traceability-matrix.md
├── workflow-status.md
└── project-metrics.md
```

---

## 6. Yêu cầu chất lượng

### Testing
- Unit coverage: ≥ 80% overall, ≥ 90% core business logic
- Mọi Must-Have AC phải có E2E test
- 0 Critical CVE, 0 High CVE — CI fail nếu có
- Accessibility: WCAG 2.1 AA

### Security
- Không hardcode secret vào bất kỳ file nào
- Chỉ commit `.env.example` (placeholder) — không commit `.env`
- SAST scan PASS trước khi merge vào develop/main
- Container scan (Trivy): 0 Critical, 0 High

### Performance Budget (Frontend)
- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Bundle size (main): < 200KB gzipped

### Accessibility
- WCAG 2.1 Level AA bắt buộc cho tất cả giao diện

---

## 7. Yêu cầu giao diện

- Framework: React / Vue / Next.js — ghi lý do trong ADR
- TypeScript bắt buộc (project hơn prototype)
- Design system đầy đủ: color tokens, typography, spacing — trong docs/04-architecture.md
- Responsive: 320px+ (mobile), 768px+ (tablet), 1024px+ (desktop)
- Không hardcode hex color / pixel size ngoài design system

---

## 8. Branching Strategy

```
main     ← production-ready, merge qua PR sau Review PASS
  └── develop  ← integration
        ├── feature/[US-ID]-[tên]
        ├── fix/[ticket-id]-[mô-tả]
        └── chore/[mô-tả]
hotfix/[HF-ID]-[mô-tả]  ← tách từ main
```

---

## 9. Commit Convention — Conventional Commits

Format: `<type>(<scope>): <description>`

| Gate PASS              | Lệnh commit đề xuất                                                   |
|-----------------------|-----------------------------------------------------------------------|
| Gate 0 — Project Init  | `git commit -m "docs(project): khởi tạo cấu trúc dự án"`            |
| Gate 1 — BA PASS       | `git commit -m "docs(ba): BA analysis PASS — [scope]"`               |
| Gate 2 — Arch PASS     | `git commit -m "docs(arch): architecture PASS — ADR và UI duyệt"`   |
| Gate 3 — Dev done      | `git commit -m "feat([scope]): implement [tên tính năng]"`           |
| Gate 4 — Test PASS     | `git commit -m "test([scope]): PASS — coverage [X]%, AC 100%"`      |
| Gate 5 — Review PASS   | `git commit -m "chore([scope]): review PASS — sẵn sàng release"`    |
| Gate 6 — Release ready | `git commit -m "chore(release): v[version] — staging verified"`     |
| Gate 7 — Deploy done   | `git commit -m "chore(deploy): v[version] → production [timestamp]"`|

Quy tắc: Workflow Controller đề xuất lệnh → chờ người dùng xác nhận → commit.

---

## 10. CI/CD Minimum

```
PR:           lint → type-check → unit test → SAST + audit
→ develop:    + build → staging deploy → E2E test
→ main:       + manual approval → production deploy → smoke test
```

---

## 11. NFR — BA Agent bắt buộc định nghĩa với target cụ thể

| Nhóm     | Phải có                                           |
|---------|---------------------------------------------------|
| Perf    | Response time p50/p95/p99, throughput             |
| Scale   | Concurrent users, data growth                     |
| Avail   | Uptime SLA (%), RTO (phút), RPO (phút)            |
| Security| Auth mechanism, encryption standard, compliance   |
| UX      | Page load budget, browser support, WCAG level     |

---

## 12. ADR — Bắt buộc cho

- Kiến trúc tổng thể, database chính, auth strategy, frontend framework, deployment platform
- File: docs/04-adr.md

---

## 13. Secrets & Configuration

| Loại              | Được commit |
|------------------|-------------|
| `.env.example`    | ✅ Có       |
| `.env`            | ❌ Không    |
| `*.tfvars` thật   | ❌ Không    |
| `*.tfstate`       | ❌ Không    |

---

## 14. Traceability

docs/traceability-matrix.md duy trì từ Gate 1 → Gate 8:
`Requirement → User Story → AC → Module → Test Case → Deploy`
