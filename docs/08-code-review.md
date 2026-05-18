# 08 — Code Review

## Scope
- Review implementation MVP hien tai trong `src/app.py`.
- Doi chieu voi BA/Architecture docs da cap nhat.

## Findings
1. Medium: Auto TTS bi goi lai nhieu lan khi Streamlit rerun.
- Impact: cau hoi bi doc lap, gay on va giam UX cho tre.
- Status: FIXED.
- Change: bo sung state `last_spoken_index`, chi auto-speak 1 lan moi cau; nut replay van hoat dong thu cong.

2. Low: Chua co test integration/e2e cho UI flow.
- Impact: nguy co loi dieu huong/man hinh khong duoc phat hien som.
- Status: OPEN (planned in next test phase).

3. Low: Chua co bo asset anh/audio rieng theo schema du lieu.
- Impact: san pham chua dat chat luong noi dung da phuong tien muc tieu.
- Status: OPEN.

## Verified Strengths
- Logic sinh cau hoi dung 4 dap an, 1 dap an dung.
- Uu tien distractor cung group noi dung.
- Co co che tranh lap cau hoi khi pool du.
- Unit tests pass cho logic cot loi.

## Review Decision
- Gate 5: PASS_WITH_MINOR_ISSUES
