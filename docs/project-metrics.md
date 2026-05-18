# Project Metrics

**Du an:** Hoc-cung-con

| Gate | Ten             | Cycle time | So lan retry | Ghi chu |
|------|----------------|------------|-------------|---------|
| 0    | Project Init   | —          | 0           | PASS |
| 1    | BA Analysis    | —          | 1           | PASS (updated by new prod description) |
| 2    | Architecture   | —          | 1           | PASS_WITH_MINOR_ISSUES |
| 3    | Development    | —          | 2           | IN_PROGRESS (fix UX auto-TTS rerun) |
| 4    | Testing        | —          | 0           | PASS_WITH_MINOR_ISSUES (7 unit tests pass) |
| 5    | Code Review    | —          | 0           | PASS_WITH_MINOR_ISSUES |
| 6    | Release Prep   | —          | 0           | PASS_WITH_MINOR_ISSUES |
| 7    | Deploy         | —          | 1           | WAITING_USER_APPROVAL (configs prepared) |

## Quality Metrics
- Defect density: chua du du lieu.
- Test coverage: chua do coverage, da co 7 unit tests pass.
- So CR phat sinh sau Gate 2: 1 (cap nhat theo prod-description moi).
- So hotfix sau deploy: 0 (chua deploy).
