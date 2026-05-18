import random
import uuid

import streamlit as st
import streamlit.components.v1 as components


LANG = {
    "vi": {
        "app_name": "Hoc Cung Con",
        "subtitle": "Be hoc mau sac, hinh hoc, chu cai, con vat va con so",
        "start": "Bat dau",
        "home": "Trang chu",
        "guide": "Huong dan phu huynh",
        "language": "Ngon ngu",
        "topic": "Chu de",
        "progress": "Cau",
        "score": "Diem",
        "replay_audio": "Nghe lai cau hoi",
        "sound_on": "Am thanh bat",
        "sound_off": "Am thanh tat",
        "correct": ["Gioi qua!", "Tuyet voi!", "Chinh xac roi!", "Con lam tot lam!"],
        "wrong": [
            "Khong sao, minh cung hoc tiep nhe!",
            "Gan dung roi, cau sau se tot hon!",
            "Co len, con dang lam rat tot!",
        ],
        "result": "Ket qua",
        "play_again": "Choi lai",
        "change_topic": "Doi chu de",
        "total": "Tong cau",
        "right": "Dung",
        "wrong_count": "Sai",
        "parent_guide_title": "Huong dan ngan cho phu huynh",
        "parent_guide_items": [
            "1) Chon ngon ngu phu hop voi be.",
            "2) Chon 1 chu de va bam Bat dau.",
            "3) Moi luot co 10 cau, moi cau 4 dap an.",
            "4) Co the bat/tat am thanh va nghe lai cau hoi.",
            "5) Ket thuc se hien thi diem va goi y cho be hoc tiep.",
        ],
        "feedback_bands": [
            (3, "Con da co gang rat tot, minh cung hoc lai nhe!"),
            (6, "Kha lam, con dang tien bo roi!"),
            (8, "Rat tot, con tra loi rat gioi!"),
            (10, "Tuyet voi, con that xuat sac!"),
        ],
    },
    "en": {
        "app_name": "Learn With Kids",
        "subtitle": "Learn colors, shapes, letters, animals and numbers",
        "start": "Start",
        "home": "Home",
        "guide": "Parent guide",
        "language": "Language",
        "topic": "Topic",
        "progress": "Question",
        "score": "Score",
        "replay_audio": "Replay question",
        "sound_on": "Sound on",
        "sound_off": "Sound off",
        "correct": ["Great job!", "Excellent!", "Well done!", "That's right!"],
        "wrong": [
            "That's okay, let's keep learning!",
            "Good try! The next one will be better!",
            "You are doing great!",
        ],
        "result": "Result",
        "play_again": "Play again",
        "change_topic": "Change topic",
        "total": "Total",
        "right": "Correct",
        "wrong_count": "Wrong",
        "parent_guide_title": "Quick guide for parents",
        "parent_guide_items": [
            "1) Choose a language for your child.",
            "2) Pick a topic then press Start.",
            "3) Each round has 10 questions with 4 options.",
            "4) You can toggle sound and replay each question.",
            "5) Final screen shows score and encouragement.",
        ],
        "feedback_bands": [
            (3, "You did a good effort. Let's learn again!"),
            (6, "Nice work, you are improving!"),
            (8, "Very good, you did great!"),
            (10, "Amazing! You are excellent!"),
        ],
    },
}


TOPIC_META = {
    "colors": {"icon": "🎨", "vi_name": "Mau sac", "en_name": "Colors"},
    "shapes": {"icon": "🔺", "vi_name": "Hinh hoc", "en_name": "Shapes"},
    "letters": {"icon": "🔤", "vi_name": "Chu cai", "en_name": "Letters"},
    "animals": {"icon": "🐾", "vi_name": "Con vat", "en_name": "Animals"},
    "numbers": {"icon": "🔢", "vi_name": "Con so", "en_name": "Numbers"},
}


DATA = {
    "colors": {
        "prompt_vi": "Con hay chon mau {item}.",
        "prompt_en": "Please choose the {item} color.",
        "items": [
            {"id": "COLOR_001", "group": "core", "vi": "do", "en": "red"},
            {"id": "COLOR_002", "group": "core", "vi": "xanh la", "en": "green"},
            {"id": "COLOR_003", "group": "core", "vi": "xanh duong", "en": "blue"},
            {"id": "COLOR_004", "group": "core", "vi": "vang", "en": "yellow"},
            {"id": "COLOR_005", "group": "core", "vi": "cam", "en": "orange"},
            {"id": "COLOR_006", "group": "core", "vi": "tim", "en": "purple"},
            {"id": "COLOR_007", "group": "core", "vi": "hong", "en": "pink"},
            {"id": "COLOR_008", "group": "core", "vi": "den", "en": "black"},
            {"id": "COLOR_009", "group": "core", "vi": "trang", "en": "white"},
            {"id": "COLOR_010", "group": "core", "vi": "nau", "en": "brown"},
            {"id": "COLOR_011", "group": "core", "vi": "xam", "en": "gray"},
        ],
    },
    "shapes": {
        "prompt_vi": "Con hay chon hinh {item}.",
        "prompt_en": "Please choose the {item}.",
        "items": [
            {"id": "SHAPE_001", "group": "flat", "vi": "tron", "en": "circle"},
            {"id": "SHAPE_002", "group": "flat", "vi": "vuong", "en": "square"},
            {"id": "SHAPE_003", "group": "flat", "vi": "tam giac", "en": "triangle"},
            {"id": "SHAPE_004", "group": "flat", "vi": "chu nhat", "en": "rectangle"},
            {"id": "SHAPE_005", "group": "flat", "vi": "ngoi sao", "en": "star"},
            {"id": "SHAPE_006", "group": "flat", "vi": "trai tim", "en": "heart"},
            {"id": "SHAPE_007", "group": "flat", "vi": "thoi", "en": "diamond"},
            {"id": "SHAPE_008", "group": "flat", "vi": "bau duc", "en": "oval"},
            {"id": "SHAPE_009", "group": "solid", "vi": "cau", "en": "sphere"},
            {"id": "SHAPE_010", "group": "solid", "vi": "lap phuong", "en": "cube"},
            {"id": "SHAPE_011", "group": "solid", "vi": "hop chu nhat", "en": "rectangular prism"},
            {"id": "SHAPE_012", "group": "solid", "vi": "tru", "en": "cylinder"},
            {"id": "SHAPE_013", "group": "solid", "vi": "non", "en": "cone"},
            {"id": "SHAPE_014", "group": "solid", "vi": "chop", "en": "pyramid"},
            {"id": "SHAPE_015", "group": "solid", "vi": "lang tru", "en": "prism"},
        ],
    },
    "letters": {
        "prompt_vi": "Con hay chon chu {item}.",
        "prompt_en": "Please choose letter {item}.",
        "items": [
            {"id": f"LETTER_VI_{idx:03d}", "group": "vi", "vi": ch, "en": ch}
            for idx, ch in enumerate(
                [
                    "A", "Ă", "Â", "B", "C", "D", "Đ", "E", "Ê", "G", "H", "I", "K", "L", "M", "N",
                    "O", "Ô", "Ơ", "P", "Q", "R", "S", "T", "U", "Ư", "V", "X", "Y",
                ],
                start=1,
            )
        ] + [{"id": f"LETTER_EN_{i:03d}", "group": "en", "vi": c, "en": c} for i, c in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), start=1)],
    },
    "animals": {
        "prompt_vi": "Con hay chon con {item}.",
        "prompt_en": "Please choose the {item}.",
        "items": [
            {"id": "ANIMAL_001", "group": "animal", "vi": "cho", "en": "dog"},
            {"id": "ANIMAL_002", "group": "animal", "vi": "meo", "en": "cat"},
            {"id": "ANIMAL_003", "group": "animal", "vi": "ga", "en": "chicken"},
            {"id": "ANIMAL_004", "group": "animal", "vi": "vit", "en": "duck"},
            {"id": "ANIMAL_005", "group": "animal", "vi": "ca", "en": "fish"},
            {"id": "ANIMAL_006", "group": "animal", "vi": "chim", "en": "bird"},
            {"id": "ANIMAL_007", "group": "animal", "vi": "voi", "en": "elephant"},
            {"id": "ANIMAL_008", "group": "animal", "vi": "ho", "en": "tiger"},
            {"id": "ANIMAL_009", "group": "animal", "vi": "su tu", "en": "lion"},
            {"id": "ANIMAL_010", "group": "animal", "vi": "khi", "en": "monkey"},
            {"id": "ANIMAL_011", "group": "animal", "vi": "bo", "en": "cow"},
            {"id": "ANIMAL_012", "group": "animal", "vi": "ngua", "en": "horse"},
            {"id": "ANIMAL_013", "group": "animal", "vi": "cuu", "en": "sheep"},
            {"id": "ANIMAL_014", "group": "animal", "vi": "de", "en": "goat"},
            {"id": "ANIMAL_015", "group": "animal", "vi": "tho", "en": "rabbit"},
            {"id": "ANIMAL_016", "group": "animal", "vi": "gau", "en": "bear"},
            {"id": "ANIMAL_017", "group": "animal", "vi": "rua", "en": "turtle"},
            {"id": "ANIMAL_018", "group": "animal", "vi": "ech", "en": "frog"},
        ],
    },
    "numbers": {
        "prompt_vi": "Con hay chon so {item}.",
        "prompt_en": "Please choose number {item}.",
        "items": [
            {"id": "NUM_001", "group": "small", "vi": "0", "en": "0"},
            {"id": "NUM_002", "group": "small", "vi": "1", "en": "1"},
            {"id": "NUM_003", "group": "small", "vi": "2", "en": "2"},
            {"id": "NUM_004", "group": "small", "vi": "3", "en": "3"},
            {"id": "NUM_005", "group": "small", "vi": "4", "en": "4"},
            {"id": "NUM_006", "group": "small", "vi": "5", "en": "5"},
            {"id": "NUM_007", "group": "small", "vi": "6", "en": "6"},
            {"id": "NUM_008", "group": "small", "vi": "7", "en": "7"},
            {"id": "NUM_009", "group": "small", "vi": "8", "en": "8"},
            {"id": "NUM_010", "group": "small", "vi": "9", "en": "9"},
            {"id": "NUM_011", "group": "small", "vi": "10", "en": "10"},
            {"id": "NUM_012", "group": "small", "vi": "12", "en": "12"},
            {"id": "NUM_013", "group": "small", "vi": "15", "en": "15"},
            {"id": "NUM_014", "group": "tens", "vi": "20", "en": "20"},
            {"id": "NUM_015", "group": "tens", "vi": "30", "en": "30"},
            {"id": "NUM_016", "group": "tens", "vi": "50", "en": "50"},
            {"id": "NUM_017", "group": "tens", "vi": "100", "en": "100"},
            {"id": "NUM_018", "group": "hundreds", "vi": "200", "en": "200"},
            {"id": "NUM_019", "group": "hundreds", "vi": "500", "en": "500"},
            {"id": "NUM_020", "group": "thousands", "vi": "1000", "en": "1000"},
            {"id": "NUM_021", "group": "thousands", "vi": "2000", "en": "2000"},
            {"id": "NUM_022", "group": "thousands", "vi": "5000", "en": "5000"},
            {"id": "NUM_023", "group": "thousands", "vi": "10000", "en": "10000"},
            {"id": "NUM_024", "group": "large_round", "vi": "20000", "en": "20000"},
            {"id": "NUM_025", "group": "large_round", "vi": "50000", "en": "50000"},
            {"id": "NUM_026", "group": "large_round", "vi": "100000", "en": "100000"},
            {"id": "NUM_027", "group": "large_round", "vi": "500000", "en": "500000"},
            {"id": "NUM_028", "group": "large_round", "vi": "1000000", "en": "1000000"},
            {"id": "NUM_029", "group": "large_round", "vi": "10000000", "en": "10000000"},
            {"id": "NUM_030", "group": "large_round", "vi": "100000000", "en": "100000000"},
            {"id": "NUM_031", "group": "large_round", "vi": "1000000000", "en": "1000000000"},
        ],
    },
}


def topic_label(topic_key: str, lang: str) -> str:
    item = TOPIC_META[topic_key]
    return f"{item['icon']} {item['vi_name'] if lang == 'vi' else item['en_name']}"


def speak(text: str, lang: str, enabled: bool) -> None:
    if not enabled:
        return
    lang_code = "vi-VN" if lang == "vi" else "en-US"
    safe = text.replace("'", "\\'")
    components.html(
        f"""
        <script>
            const u = new SpeechSynthesisUtterance('{safe}');
            u.lang = '{lang_code}';
            u.rate = 0.9;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(u);
        </script>
        """,
        height=0,
    )


def get_topic_pool(topic: str, lang: str):
    all_items = DATA[topic]["items"]
    if topic == "letters":
        # Chon bo chu theo ngon ngu da chon
        target_group = "vi" if lang == "vi" else "en"
        return [x for x in all_items if x["group"] == target_group]
    return all_items


def build_round(lang: str, topic: str, size: int = 10):
    topic_data = DATA[topic]
    prompt_tpl = topic_data["prompt_vi"] if lang == "vi" else topic_data["prompt_en"]
    pool = get_topic_pool(topic, lang)

    if len(pool) < 4:
        raise ValueError("Pool du lieu khong du de tao 4 dap an")

    # Tranh lap cau hoi trong 1 luot neu co the
    sample_size = min(size, len(pool))
    selected = random.sample(pool, k=sample_size)

    # Neu pool < size, bo sung bang cach lay ngau nhien co lap de du 10 cau
    while len(selected) < size:
        selected.append(random.choice(pool))

    questions = []
    for correct in selected:
        same_group = [x for x in pool if x["id"] != correct["id"] and x["group"] == correct["group"]]
        backup_group = [x for x in pool if x["id"] != correct["id"]]

        wrong_source = same_group if len(same_group) >= 3 else backup_group
        wrongs = random.sample(wrong_source, k=3)

        correct_label = correct["vi"] if lang == "vi" else correct["en"]
        options = [w["vi"] if lang == "vi" else w["en"] for w in wrongs] + [correct_label]
        random.shuffle(options)

        questions.append(
            {
                "prompt": prompt_tpl.format(item=correct_label),
                "correct": correct_label,
                "options": options,
                "correct_id": correct["id"],
            }
        )
    return questions


def init_state():
    st.session_state.setdefault("screen", "home")
    st.session_state.setdefault("lang", "vi")
    st.session_state.setdefault("topic", "colors")
    st.session_state.setdefault("sound", True)
    st.session_state.setdefault("round", [])
    st.session_state.setdefault("index", 0)
    st.session_state.setdefault("score", 0)
    st.session_state.setdefault("last_message", "")
    st.session_state.setdefault("last_type", "")
    st.session_state.setdefault("last_spoken_index", -1)


def start_round():
    st.session_state.round = build_round(st.session_state.lang, st.session_state.topic, 10)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.last_message = ""
    st.session_state.last_type = ""
    st.session_state.last_spoken_index = -1
    st.session_state.screen = "quiz"


def grade_feedback(score: int, lang: str) -> str:
    bands = LANG[lang]["feedback_bands"]
    for limit, text in bands:
        if score <= limit:
            return text
    return bands[-1][1]


def render_parent_guide():
    lang = st.session_state.lang
    t = LANG[lang]

    st.title("📘 " + t["parent_guide_title"])
    for item in t["parent_guide_items"]:
        st.write(item)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🏠 " + t["home"], use_container_width=True):
            st.session_state.screen = "home"
            st.rerun()
    with c2:
        if st.button("🚀 " + t["start"], use_container_width=True):
            start_round()
            st.rerun()


def render_home():
    lang = st.session_state.lang
    t = LANG[lang]
    st.title(f"🌈 {t['app_name']}")
    st.caption(t["subtitle"])

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.lang = "vi" if st.button("🇻🇳 Tieng Viet", use_container_width=True) else st.session_state.lang
    with col2:
        st.session_state.lang = "en" if st.button("🇺🇸 English", use_container_width=True) else st.session_state.lang

    lang = st.session_state.lang
    t = LANG[lang]
    st.subheader(f"1) {t['topic']}")
    topic_keys = list(TOPIC_META.keys())
    labels = [topic_label(k, lang) for k in topic_keys]
    selected = st.radio(label=t["topic"], options=topic_keys, format_func=lambda x: labels[topic_keys.index(x)], horizontal=False)
    st.session_state.topic = selected

    st.subheader("2) " + t["sound_on"] + "/" + t["sound_off"])
    st.session_state.sound = st.toggle("🔊", value=st.session_state.sound, label_visibility="collapsed")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 " + t["start"], use_container_width=True):
            start_round()
            st.rerun()
    with c2:
        if st.button("👨‍👩‍👧 " + t["guide"], use_container_width=True):
            st.session_state.screen = "guide"
            st.rerun()


def render_quiz():
    lang = st.session_state.lang
    t = LANG[lang]
    q = st.session_state.round[st.session_state.index]
    current = st.session_state.index + 1

    st.subheader(f"{t['progress']} {current}/10")
    st.progress(current / 10)
    st.write(f"**{t['score']}: {st.session_state.score}**")

    st.markdown(f"### {q['prompt']}")
    if st.button("🔁 " + t["replay_audio"], use_container_width=True):
        speak(q["prompt"], lang, st.session_state.sound)

    if st.session_state.last_spoken_index != st.session_state.index:
        speak(q["prompt"], lang, st.session_state.sound)
        st.session_state.last_spoken_index = st.session_state.index

    cols = st.columns(2)
    for i, opt in enumerate(q["options"]):
        with cols[i % 2]:
            if st.button(opt, key=f"opt_{st.session_state.index}_{i}", use_container_width=True):
                if opt == q["correct"]:
                    st.session_state.score += 1
                    st.session_state.last_message = random.choice(t["correct"])
                    st.session_state.last_type = "success"
                else:
                    st.session_state.last_message = f"{random.choice(t['wrong'])} ({q['correct']})"
                    st.session_state.last_type = "warning"

                st.session_state.index += 1
                if st.session_state.index >= len(st.session_state.round):
                    st.session_state.screen = "result"
                st.rerun()

    if st.session_state.last_message:
        if st.session_state.last_type == "success":
            st.success(st.session_state.last_message)
        else:
            st.warning(st.session_state.last_message)

    c1, c2 = st.columns(2)
    with c1:
        st.session_state.sound = st.toggle("🔊", value=st.session_state.sound, key="quiz_sound")
    with c2:
        if st.button("🏠 " + t["home"], use_container_width=True):
            st.session_state.screen = "home"
            st.rerun()


def render_result():
    lang = st.session_state.lang
    t = LANG[lang]
    score = st.session_state.score
    wrong = 10 - score

    st.title("🏁 " + t["result"])
    st.write(f"**{t['total']}: 10**")
    st.write(f"**{t['right']}: {score}**")
    st.write(f"**{t['wrong_count']}: {wrong}**")
    st.write(f"**{t['score']}: {score}/10**")
    st.info(grade_feedback(score, lang))

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🔁 " + t["play_again"], use_container_width=True):
            start_round()
            st.rerun()
    with c2:
        if st.button("🧩 " + t["change_topic"], use_container_width=True):
            st.session_state.screen = "home"
            st.rerun()
    with c3:
        if st.button("🏠 " + t["home"], use_container_width=True):
            st.session_state.screen = "home"
            st.rerun()


def main():
    st.set_page_config(page_title="Hoc Cung Con", page_icon="🌈", layout="centered")
    st.markdown(
        """
        <style>
            .stButton button {height: 56px; font-size: 1.1rem; border-radius: 14px;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    init_state()

    if st.session_state.screen == "home":
        render_home()
    elif st.session_state.screen == "guide":
        render_parent_guide()
    elif st.session_state.screen == "quiz":
        render_quiz()
    else:
        render_result()


if __name__ == "__main__":
    main()
