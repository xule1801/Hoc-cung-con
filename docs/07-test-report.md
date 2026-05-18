# 07 — Test Report

## Scope
- Unit tests cho business logic trong `src/app.py`.
- Tap trung vao cac ham:
  - `get_topic_pool`
  - `build_round`
  - `grade_feedback`

## Test Cases Executed
1. `test_get_topic_pool_letters_respects_language`
2. `test_build_round_basic_structure`
3. `test_build_round_no_repeat_when_pool_is_enough`
4. `test_shapes_wrong_answers_prefer_same_group`
5. `test_grade_feedback_band_mapping`
6. `test_build_round_allows_repeat_when_size_exceeds_pool`
7. `test_build_round_raises_with_too_small_pool`

## Execution
- Command: `python3 -m unittest discover -s tests/unit -p 'test_*.py'`
- Result: PASS
- Summary: 7 tests, 0 failed, 0 errors

## Findings
- Logic sinh cau hoi dap ung quy tac 4 dap an, uu tien cung group.
- Co co che tranh lap cau hoi khi pool du lon.
- Co xu ly loi khi pool du lieu khong du cho 4 dap an.

## Gaps / Risks
- Chua co do luong coverage phan tram.
- Chua co integration/e2e tests cho UI flow Streamlit.
- Chua test runtime TTS tren trinh duyet that.

## Gate 4 Decision
- PASS_WITH_MINOR_ISSUES
