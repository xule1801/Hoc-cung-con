# 06 — Dev Notes (Updated)

## Scope implemented
- MVP Streamlit cho tre 2-4 tuoi, 2 ngon ngu, 5 chu de.
- Flow day du: Home -> Parent Guide -> Quiz (10 cau) -> Result.
- Rules sinh cau hoi theo chu de, uu tien distractor cung group, tranh lap cau hoi neu pool du.
- Scoring va feedback theo thang diem 0-10.
- TTS cau hoi (Web Speech API) + toggle am thanh.

## Key technical updates
- Refactor tu `CONTENT` sang `TOPIC_META + DATA` schema `id/group/vi/en`.
- Bo sung dataset theo mo ta moi: colors (co nau/xam), shapes flat+solid, animals mo rong, numbers toi 1,000,000,000 (so tron lon).
- Bo sung parent guide screen.
- Bo sung unit tests cho logic sinh cau hoi va feedback.

## Files changed in this round
- docs/02-ba-analysis.md
- docs/04-architecture.md
- docs/05-ba-architecture-validation.md
- docs/06-dev-notes.md
- docs/traceability-matrix.md
- src/app.py
- tests/unit/test_app_logic.py

## Verification
- `python3 -m py_compile src/app.py` PASS.
- `python3 -m unittest discover -s tests/unit -p 'test_*.py'` PASS (5 tests).

## Notes
- Chua co image/audio assets rieng va e2e automation.
