# 09 — Release Report

## Release Info
- Project: Hoc-cung-con
- Release type: MVP internal release candidate
- Date: 2026-05-18
- Version tag: v0.1.0-rc1 (proposed)

## Selected Deployment Platform
- Platform: Streamlit Community Cloud (FREE)
- Selection date: 2026-05-18
- Reason: phu hop nhat voi runtime Streamlit, setup nhanh, free tier ro rang.

## Scope Included
- Streamlit web app cho tre 2-4 tuoi.
- 2 ngon ngu: VI/EN.
- 5 chu de: colors, shapes, letters, animals, numbers.
- 10 cau/luot, 4 dap an/cau, scoring va result feedback.
- Parent guide screen.
- TTS cau hoi + replay + sound toggle.

## Build & Test Status
- Syntax check: PASS (`python3 -m py_compile src/app.py`)
- Unit tests: PASS (`7/7`)
- Integration tests: NOT RUN
- E2E tests: NOT RUN
- Coverage report: NOT AVAILABLE

## Streamlit Deploy Inputs
- Repository: `<your-github-repo>`
- Branch: `main` (or branch ban muon deploy)
- Main file path: `src/app.py`
- Python dependencies: `requirements.txt`

## Pre-release Checklist
- [x] BA doc updated (`02`)
- [x] Architecture doc updated (`04`, `05`)
- [x] Dev notes updated (`06`)
- [x] Test report available (`07`)
- [x] Code review report available (`08`)
- [x] Local run instructions in README
- [ ] Coverage >= 80% (chua dat/khong do)
- [ ] Integration/E2E smoke suite
- [ ] Static asset pack (image/audio) production-ready

## Known Issues
1. Chua co coverage metric.
2. Chua co integration/e2e automation.
3. Chua co image/audio asset rieng theo schema noi dung.
4. Chua co background music va feedback sound files.

## Gate 6 Decision
- PASS_WITH_MINOR_ISSUES
- Gate 7 co the thuc hien deploy len Streamlit Community Cloud.
