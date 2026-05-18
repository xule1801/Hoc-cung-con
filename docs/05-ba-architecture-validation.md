# 05 — BA Architecture Validation (Updated)

## Validation Summary
- Da doi chieu `02-ba-analysis.md` (ban cap nhat) voi `04-architecture.md` va implementation `src/app.py`.
- Ket qua: dap ung pham vi MVP va cac AC chinh, con mot so minor gap phi chuc nang.

## Requirement Mapping
- AC-01: `render_home` cho phep chon ngon ngu + chu de + start.
- AC-02: `build_round(..., size=10)` dam bao 10 cau moi luot.
- AC-03: moi question co 4 options, 1 correct.
- AC-04: `random.sample` trong `build_round` tranh lap cau hoi khi pool du.
- AC-05: distractor uu tien cung `group` (flat/solid, number groups...).
- AC-06: scoring logic trong `render_quiz` (correct +1, wrong +0).
- AC-07: `render_result` + `grade_feedback` theo 4 band diem.
- AC-08: `render_parent_guide` da duoc bo sung.

## Minor Gaps
- Chua noi day du schema asset (`image/audio_vi/audio_en`) o runtime.
- Chua co am thanh nen va phan hoi dung/sai bang file audio rieng.
- Chua co test suite tu dong cho cac AC.

## Decision
- Gate 2 Validation: PASS_WITH_MINOR_ISSUES
