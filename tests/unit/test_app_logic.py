import os
import sys
import types
import unittest


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Minimal streamlit stub for importing app logic in unit tests.
streamlit_mod = types.ModuleType("streamlit")
streamlit_mod.session_state = {}
streamlit_mod.set_page_config = lambda *args, **kwargs: None
streamlit_mod.markdown = lambda *args, **kwargs: None

components_pkg = types.ModuleType("streamlit.components")
components_v1_mod = types.ModuleType("streamlit.components.v1")
components_v1_mod.html = lambda *args, **kwargs: None
components_pkg.v1 = components_v1_mod
streamlit_mod.components = components_pkg

sys.modules.setdefault("streamlit", streamlit_mod)
sys.modules.setdefault("streamlit.components", components_pkg)
sys.modules.setdefault("streamlit.components.v1", components_v1_mod)

import app  # noqa: E402


class AppLogicTests(unittest.TestCase):
    def test_get_topic_pool_letters_respects_language(self):
        vi_pool = app.get_topic_pool("letters", "vi")
        en_pool = app.get_topic_pool("letters", "en")
        self.assertEqual(len(vi_pool), 29)
        self.assertEqual(len(en_pool), 26)
        self.assertTrue(all(item["group"] == "vi" for item in vi_pool))
        self.assertTrue(all(item["group"] == "en" for item in en_pool))

    def test_build_round_basic_structure(self):
        questions = app.build_round("vi", "colors", size=10)
        self.assertEqual(len(questions), 10)
        for q in questions:
            self.assertEqual(len(q["options"]), 4)
            self.assertIn(q["correct"], q["options"])

    def test_build_round_no_repeat_when_pool_is_enough(self):
        questions = app.build_round("en", "colors", size=10)
        correct_ids = [q["correct_id"] for q in questions]
        self.assertEqual(len(set(correct_ids)), 10)

    def test_shapes_wrong_answers_prefer_same_group(self):
        pool = app.get_topic_pool("shapes", "en")
        label_to_group = {item["en"]: item["group"] for item in pool}
        questions = app.build_round("en", "shapes", size=10)
        for q in questions:
            correct_group = label_to_group[q["correct"]]
            wrong_groups = [label_to_group[opt] for opt in q["options"] if opt != q["correct"]]
            self.assertTrue(all(g == correct_group for g in wrong_groups))

    def test_grade_feedback_band_mapping(self):
        self.assertEqual(app.grade_feedback(0, "vi"), app.LANG["vi"]["feedback_bands"][0][1])
        self.assertEqual(app.grade_feedback(4, "vi"), app.LANG["vi"]["feedback_bands"][1][1])
        self.assertEqual(app.grade_feedback(8, "vi"), app.LANG["vi"]["feedback_bands"][2][1])
        self.assertEqual(app.grade_feedback(10, "vi"), app.LANG["vi"]["feedback_bands"][3][1])

    def test_build_round_allows_repeat_when_size_exceeds_pool(self):
        questions = app.build_round("en", "colors", size=12)
        self.assertEqual(len(questions), 12)
        correct_ids = [q["correct_id"] for q in questions]
        self.assertLess(len(set(correct_ids)), 12)

    def test_build_round_raises_with_too_small_pool(self):
        backup = app.DATA["colors"]["items"]
        try:
            app.DATA["colors"]["items"] = [
                {"id": "TMP_1", "group": "core", "vi": "m1", "en": "m1"},
                {"id": "TMP_2", "group": "core", "vi": "m2", "en": "m2"},
                {"id": "TMP_3", "group": "core", "vi": "m3", "en": "m3"},
            ]
            with self.assertRaises(ValueError):
                app.build_round("vi", "colors", size=10)
        finally:
            app.DATA["colors"]["items"] = backup


if __name__ == "__main__":
    unittest.main()
