# 04 — Architecture (Updated)

## Technical Decision
- Framework: Streamlit (Python) de trien khai nhanh MVP web app.
- Runtime: 1 web process, state luu trong `st.session_state`.
- Data layer: in-memory dataset trong ma nguon (chua dung DB o phase nay).

## Screen Flow
- `home` -> `guide` (optional) -> `quiz` -> `result`
- Tu `result`: choi lai / doi chu de / ve trang chu.

## Modules (src/app.py)
- `LANG`: i18n labels + feedback VI/EN.
- `TOPIC_META`: metadata hien thi chu de.
- `DATA`: noi dung hoc theo chu de voi schema item co `id/group/vi/en`.
- `get_topic_pool(topic, lang)`: loc pool theo ngon ngu (dac biet voi letters).
- `build_round(lang, topic, size=10)`: sinh 10 cau, tron dap an, uu tien distractor cung group, tranh lap cau hoi neu pool du.
- `render_home()`: chon ngon ngu, chu de, am thanh, dieu huong.
- `render_parent_guide()`: man hinh huong dan phu huynh.
- `render_quiz()`: man hinh cau hoi + 4 dap an + cham diem.
- `render_result()`: tong ket diem + khuyen khich.
- `speak(...)`: nhung Web Speech API cho doc cau hoi.

## Data Model (in-memory)
- ContentItem
  - `id`: string
  - `group`: string (vd `flat`, `solid`, `large_round`)
  - `vi`: string
  - `en`: string
- Question
  - `prompt`: string
  - `correct`: string
  - `options`: list[string], len=4
  - `correct_id`: string

## Question Generation Rules
- Lay cau hoi theo dung chu de da chon.
- Moi cau co 1 dap an dung + 3 dap an sai.
- Dap an sai uu tien cung `group` voi dap an dung.
- Thu tu dap an duoc xao tron.
- Trong 1 luot 10 cau, tranh lap cau hoi neu pool du lon.

## Current Gaps
- Chua co bo anh/audio asset rieng theo bang schema noi dung.
- Chua co nhac nen va sound effect dung/sai.
- Chua co test automation cho unit/e2e.

## Gate 2 Conclusion
- PASS_WITH_MINOR_ISSUES (minor gaps ve asset va test)
