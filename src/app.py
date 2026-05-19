import random
import base64
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
try:
    from streamlit_clickable_images import clickable_images
except ModuleNotFoundError:
    clickable_images = None


ASSET_DIR = Path(__file__).resolve().parent.parent / "assets" / "images"
AUDIO_DIR = Path(__file__).resolve().parent.parent / "assets" / "audio"

def img(path: str) -> str:
    return str(ASSET_DIR / path)


def to_data_uri(path: str) -> str:
    mime, _ = mimetypes.guess_type(path)
    if mime is None:
        mime = "image/png"
    data = Path(path).read_bytes()
    encoded = base64.b64encode(data).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def render_bgm():
    bgm_path = AUDIO_DIR / "bgm.mp3"
    if not bgm_path.exists():
        return
    b64 = base64.b64encode(bgm_path.read_bytes()).decode()
    html_str = f"""
    <script>
        var parentDoc = window.parent.document;
        if (!parentDoc.getElementById("my-bgm")) {{
            var audio = parentDoc.createElement("audio");
            audio.id = "my-bgm";
            audio.src = "data:audio/mp3;base64,{b64}";
            audio.loop = true;
            audio.volume = 0.4;
            parentDoc.body.appendChild(audio);
            
            var playPromise = audio.play();
            if (playPromise !== undefined) {{
                playPromise.catch(function(error) {{
                    parentDoc.addEventListener("click", function() {{
                        audio.play();
                    }}, {{once: true}});
                }});
            }}
        }}
    </script>
    """
    st.components.v1.html(html_str, width=0, height=0)


def render_fireworks():
    applause_path = AUDIO_DIR / "applause.mp3"
    audio_js = ""
    if applause_path.exists():
        b64 = base64.b64encode(applause_path.read_bytes()).decode()
        audio_js = f"""
        var parentDoc = window.parent.document;
        var audio = parentDoc.createElement("audio");
        audio.src = "data:audio/mp3;base64,{b64}";
        audio.volume = 0.8;
        parentDoc.body.appendChild(audio);
        var playPromise = audio.play();
        if (playPromise !== undefined) {{
            playPromise.catch(function(e) {{ console.log(e); }});
        }}
        setTimeout(function() {{ audio.remove(); }}, 10000);
        """
        
    html_str = f"""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
      {audio_js}
      var duration = 3 * 1000;
      var end = Date.now() + duration;
      (function frame() {{
        confetti({{ particleCount: 5, angle: 60, spread: 55, origin: {{ x: 0 }}, colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00'] }});
        confetti({{ particleCount: 5, angle: 120, spread: 55, origin: {{ x: 1 }}, colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00'] }});
        if (Date.now() < end) {{ requestAnimationFrame(frame); }}
      }}());
    </script>
    """
    st.components.v1.html(html_str, width=0, height=0)







LANG = {
    "vi": {
        "app_name": "Học Cùng Con",
        "subtitle": "Bé học màu sắc, hình học, chữ cái, con vật và con số",
        "start": "Bắt đầu",
        "home": "Trang chủ",
        "guide": "Hướng dẫn phụ huynh",
        "topic": "Chủ đề",
        "progress": "Câu",
        "score": "Điểm",
        "replay_audio": "Nghe lại câu hỏi",
        "sound_on": "Âm thanh bật",
        "sound_off": "Âm thanh tắt",
        "select": "Chọn",
        "next_question": "Câu tiếp theo",
        "tap_hint": "👆 Bé chạm trực tiếp vào hình để chọn đáp án",
        "correct": ["Giỏi quá!", "Tuyệt vời!", "Chính xác rồi!", "Con làm tốt lắm!"],
        "wrong": [
            "Không sao, mình cùng học tiếp nhé!",
            "Gần đúng rồi, câu sau sẽ tốt hơn!",
            "Cố lên, con đang làm rất tốt!",
        ],
        "result": "Kết quả",
        "play_again": "Chơi lại",
        "change_topic": "Đổi chủ đề",
        "total": "Tổng câu",
        "right": "Đúng",
        "wrong_count": "Sai",
        "parent_guide_title": "Hướng dẫn ngắn cho phụ huynh",
        "parent_guide_items": [
            "1) Chọn ngôn ngữ phù hợp với bé.",
            "2) Chọn 1 chủ đề và bấm Bắt đầu.",
            "3) Mỗi lượt có 10 câu, mỗi câu 4 đáp án bằng hình ảnh.",
            "4) Có thể bật/tắt âm thanh và nghe lại câu hỏi.",
            "5) Kết thúc sẽ hiển thị điểm và gợi ý cho bé học tiếp.",
        ],
        "feedback_bands": [
            (3, "Con đã cố gắng rất tốt, mình cùng học lại nhé!"),
            (6, "Khá lắm, con đang tiến bộ rồi!"),
            (8, "Rất tốt, con trả lời rất giỏi!"),
            (10, "Tuyệt vời, con thật xuất sắc!"),
        ],
    },
    "en": {
        "app_name": "Learn With Kids",
        "subtitle": "Learn colors, shapes, letters, animals and numbers",
        "start": "Start",
        "home": "Home",
        "guide": "Parent guide",
        "topic": "Topic",
        "progress": "Question",
        "score": "Score",
        "replay_audio": "Replay question",
        "sound_on": "Sound on",
        "sound_off": "Sound off",
        "select": "Select",
        "next_question": "Next question",
        "tap_hint": "👆 Tap directly on an image to choose",
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
            "3) Each round has 10 image-based questions with 4 options.",
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
    "colors": {"icon": "🎨", "vi_name": "Màu sắc", "en_name": "Colors"},
    "shapes": {"icon": "🔺", "vi_name": "Hình học", "en_name": "Shapes"},
    "letters": {"icon": "🔤", "vi_name": "Chữ cái", "en_name": "Letters"},
    "animals": {"icon": "🐾", "vi_name": "Con vật", "en_name": "Animals"},
    "numbers": {"icon": "🔢", "vi_name": "Con số", "en_name": "Numbers"},
}


DATA = {
    "colors": {
        "prompt_vi": "Con hãy chọn màu {item}.",
        "prompt_en": "Please choose the {item} color.",
        "items": [
            {"id": "COLOR_001", "group": "core", "vi": "đỏ", "en": "red", "image": img("colors/red.png")},
            {"id": "COLOR_002", "group": "core", "vi": "xanh lá", "en": "green", "image": img("colors/green.png")},
            {"id": "COLOR_003", "group": "core", "vi": "xanh dương", "en": "blue", "image": img("colors/blue.png")},
            {"id": "COLOR_004", "group": "core", "vi": "vàng", "en": "yellow", "image": img("colors/yellow.png")},
            {"id": "COLOR_005", "group": "core", "vi": "cam", "en": "orange", "image": img("colors/orange.png")},
            {"id": "COLOR_006", "group": "core", "vi": "tím", "en": "purple", "image": img("colors/purple.png")},
            {"id": "COLOR_007", "group": "core", "vi": "hồng", "en": "pink", "image": img("colors/pink.png")},
            {"id": "COLOR_008", "group": "core", "vi": "đen", "en": "black", "image": img("colors/black.png")},
            {"id": "COLOR_009", "group": "core", "vi": "trắng", "en": "white", "image": img("colors/white.png")},
            {"id": "COLOR_010", "group": "core", "vi": "nâu", "en": "brown", "image": img("colors/brown.png")},
            {"id": "COLOR_011", "group": "core", "vi": "xám", "en": "gray", "image": img("colors/gray.png")},
        ],
    },
    "shapes": {
        "prompt_vi": "Con hãy chọn hình {item}.",
        "prompt_en": "Please choose the {item}.",
        "items": [
            {"id": "SHAPE_001", "group": "flat", "vi": "tròn", "en": "circle", "image": img("shapes/circle.png")},
            {"id": "SHAPE_002", "group": "flat", "vi": "vuông", "en": "square", "image": img("shapes/square.png")},
            {"id": "SHAPE_003", "group": "flat", "vi": "tam giác", "en": "triangle", "image": img("shapes/triangle.png")},
            {"id": "SHAPE_004", "group": "flat", "vi": "chữ nhật", "en": "rectangle", "image": img("shapes/rectangle.png")},
            {"id": "SHAPE_005", "group": "flat", "vi": "ngôi sao", "en": "star", "image": img("shapes/star.png")},
            {"id": "SHAPE_006", "group": "flat", "vi": "trái tim", "en": "heart", "image": img("shapes/heart.png")},
            {"id": "SHAPE_007", "group": "flat", "vi": "hình thoi", "en": "diamond", "image": img("shapes/diamond.png")},
            {"id": "SHAPE_008", "group": "flat", "vi": "bầu dục", "en": "oval", "image": img("shapes/oval.png")},
            {"id": "SHAPE_009", "group": "solid", "vi": "cầu", "en": "sphere", "image": img("shapes/sphere.png")},
            {"id": "SHAPE_010", "group": "solid", "vi": "lập phương", "en": "cube", "image": img("shapes/cube.png")},
            {"id": "SHAPE_011", "group": "solid", "vi": "hộp chữ nhật", "en": "rectangular prism", "image": img("shapes/rect_prism.png")},
            {"id": "SHAPE_012", "group": "solid", "vi": "trụ", "en": "cylinder", "image": img("shapes/cylinder.png")},
            {"id": "SHAPE_013", "group": "solid", "vi": "nón", "en": "cone", "image": img("shapes/cone.png")},
            {"id": "SHAPE_014", "group": "solid", "vi": "chóp", "en": "pyramid", "image": img("shapes/pyramid.png")},
            {"id": "SHAPE_015", "group": "solid", "vi": "lăng trụ", "en": "prism", "image": img("shapes/prism.png")},
        ],
    },
    "letters": {
        "prompt_vi": "Con hãy chọn chữ {item}.",
        "prompt_en": "Please choose letter {item}.",
        "items": [
            {"id": f"LETTER_VI_{idx:03d}", "group": "vi", "vi": ch, "en": ch, "image": img(f"letters/vi_{idx:03d}.png")}
            for idx, ch in enumerate(
                [
                    "A", "Ă", "Â", "B", "C", "D", "Đ", "E", "Ê", "G", "H", "I", "K", "L", "M", "N",
                    "O", "Ô", "Ơ", "P", "Q", "R", "S", "T", "U", "Ư", "V", "X", "Y",
                ],
                start=1,
            )
        ]
        + [
            {"id": f"LETTER_EN_{i:03d}", "group": "en", "vi": c, "en": c, "image": img(f"letters/en_{i:03d}.png")}
            for i, c in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), start=1)
        ],
    },
    "animals": {
        "prompt_vi": "Con hãy chọn con {item}.",
        "prompt_en": "Please choose the {item}.",
        "items": [
            {"id": "ANIMAL_001", "group": "animal", "vi": "chó", "en": "dog", "image": img("animals/dog.png")},
            {"id": "ANIMAL_002", "group": "animal", "vi": "mèo", "en": "cat", "image": img("animals/cat.png")},
            {"id": "ANIMAL_003", "group": "animal", "vi": "gà", "en": "chicken", "image": img("animals/chicken.png")},
            {"id": "ANIMAL_004", "group": "animal", "vi": "vịt", "en": "duck", "image": img("animals/duck.png")},
            {"id": "ANIMAL_005", "group": "animal", "vi": "cá", "en": "fish", "image": img("animals/fish.png")},
            {"id": "ANIMAL_006", "group": "animal", "vi": "chim", "en": "bird", "image": img("animals/bird.png")},
            {"id": "ANIMAL_007", "group": "animal", "vi": "voi", "en": "elephant", "image": img("animals/elephant.png")},
            {"id": "ANIMAL_008", "group": "animal", "vi": "hổ", "en": "tiger", "image": img("animals/tiger.png")},
            {"id": "ANIMAL_009", "group": "animal", "vi": "sư tử", "en": "lion", "image": img("animals/lion.png")},
            {"id": "ANIMAL_010", "group": "animal", "vi": "khỉ", "en": "monkey", "image": img("animals/monkey.png")},
            {"id": "ANIMAL_011", "group": "animal", "vi": "bò", "en": "cow", "image": img("animals/cow.png")},
            {"id": "ANIMAL_012", "group": "animal", "vi": "ngựa", "en": "horse", "image": img("animals/horse.png")},
            {"id": "ANIMAL_013", "group": "animal", "vi": "cừu", "en": "sheep", "image": img("animals/sheep.png")},
            {"id": "ANIMAL_014", "group": "animal", "vi": "dê", "en": "goat", "image": img("animals/goat.png")},
            {"id": "ANIMAL_015", "group": "animal", "vi": "thỏ", "en": "rabbit", "image": img("animals/rabbit.png")},
            {"id": "ANIMAL_016", "group": "animal", "vi": "gấu", "en": "bear", "image": img("animals/bear.png")},
            {"id": "ANIMAL_017", "group": "animal", "vi": "rùa", "en": "turtle", "image": img("animals/turtle.png")},
            {"id": "ANIMAL_018", "group": "animal", "vi": "ếch", "en": "frog", "image": img("animals/frog.png")},
        ],
    },
    "numbers": {
        "prompt_vi": "Con hãy chọn số {item}.",
        "prompt_en": "Please choose number {item}.",
        "items": [
            {"id": "NUM_001", "group": "small", "vi": "0", "en": "0", "image": img("numbers/0.png")},
            {"id": "NUM_002", "group": "small", "vi": "1", "en": "1", "image": img("numbers/1.png")},
            {"id": "NUM_003", "group": "small", "vi": "2", "en": "2", "image": img("numbers/2.png")},
            {"id": "NUM_004", "group": "small", "vi": "3", "en": "3", "image": img("numbers/3.png")},
            {"id": "NUM_005", "group": "small", "vi": "4", "en": "4", "image": img("numbers/4.png")},
            {"id": "NUM_006", "group": "small", "vi": "5", "en": "5", "image": img("numbers/5.png")},
            {"id": "NUM_007", "group": "small", "vi": "6", "en": "6", "image": img("numbers/6.png")},
            {"id": "NUM_008", "group": "small", "vi": "7", "en": "7", "image": img("numbers/7.png")},
            {"id": "NUM_009", "group": "small", "vi": "8", "en": "8", "image": img("numbers/8.png")},
            {"id": "NUM_010", "group": "small", "vi": "9", "en": "9", "image": img("numbers/9.png")},
            {"id": "NUM_011", "group": "small", "vi": "10", "en": "10", "image": img("numbers/10.png")},
            {"id": "NUM_012", "group": "small", "vi": "12", "en": "12", "image": img("numbers/12.png")},
            {"id": "NUM_013", "group": "small", "vi": "15", "en": "15", "image": img("numbers/15.png")},
            {"id": "NUM_014", "group": "tens", "vi": "20", "en": "20", "image": img("numbers/20.png")},
            {"id": "NUM_015", "group": "tens", "vi": "30", "en": "30", "image": img("numbers/30.png")},
            {"id": "NUM_016", "group": "tens", "vi": "50", "en": "50", "image": img("numbers/50.png")},
            {"id": "NUM_017", "group": "tens", "vi": "100", "en": "100", "image": img("numbers/100.png")},
            {"id": "NUM_018", "group": "hundreds", "vi": "200", "en": "200", "image": img("numbers/200.png")},
            {"id": "NUM_019", "group": "hundreds", "vi": "500", "en": "500", "image": img("numbers/500.png")},
            {"id": "NUM_020", "group": "thousands", "vi": "1000", "en": "1000", "image": img("numbers/1000.png")},
            {"id": "NUM_021", "group": "thousands", "vi": "2000", "en": "2000", "image": img("numbers/2000.png")},
            {"id": "NUM_022", "group": "thousands", "vi": "5000", "en": "5000", "image": img("numbers/5000.png")},
            {"id": "NUM_023", "group": "thousands", "vi": "10000", "en": "10000", "image": img("numbers/10000.png")},
            {"id": "NUM_024", "group": "large_round", "vi": "20000", "en": "20000", "image": img("numbers/20000.png")},
            {"id": "NUM_025", "group": "large_round", "vi": "50000", "en": "50000", "image": img("numbers/50000.png")},
            {"id": "NUM_026", "group": "large_round", "vi": "100000", "en": "100000", "image": img("numbers/100000.png")},
            {"id": "NUM_027", "group": "large_round", "vi": "500000", "en": "500000", "image": img("numbers/500000.png")},
            {"id": "NUM_028", "group": "large_round", "vi": "1000000", "en": "1000000", "image": img("numbers/1000000.png")},
            {"id": "NUM_029", "group": "large_round", "vi": "10000000", "en": "10000000", "image": img("numbers/10000000.png")},
            {"id": "NUM_030", "group": "large_round", "vi": "100000000", "en": "100000000", "image": img("numbers/100000000.png")},
            {"id": "NUM_031", "group": "large_round", "vi": "1000000000", "en": "1000000000", "image": img("numbers/1000000000.png")},
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
        target_group = "vi" if lang == "vi" else "en"
        return [x for x in all_items if x["group"] == target_group]
    return all_items


def build_round(lang: str, topic: str, size: int = 10):
    topic_data = DATA[topic]
    prompt_tpl = topic_data["prompt_vi"] if lang == "vi" else topic_data["prompt_en"]
    pool = get_topic_pool(topic, lang)

    if len(pool) < 4:
        raise ValueError("Pool dữ liệu không đủ để tạo 4 đáp án")

    sample_size = min(size, len(pool))
    selected = random.sample(pool, k=sample_size)
    while len(selected) < size:
        selected.append(random.choice(pool))

    questions = []
    for correct in selected:
        same_group = [x for x in pool if x["id"] != correct["id"] and x["group"] == correct["group"]]
        backup_group = [x for x in pool if x["id"] != correct["id"]]
        wrong_source = same_group if len(same_group) >= 3 else backup_group
        wrongs = random.sample(wrong_source, k=3)

        all_options = wrongs + [correct]
        random.shuffle(all_options)

        correct_label = correct["vi"] if lang == "vi" else correct["en"]
        questions.append(
            {
                "prompt": prompt_tpl.format(item=correct_label),
                "correct": correct_label,
                "options": [o["vi"] if lang == "vi" else o["en"] for o in all_options],
                "option_images": [o["image"] for o in all_options],
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
    st.session_state.setdefault("feedback_spoken_index", -1)
    st.session_state.setdefault("answer_locked", False)
    st.session_state.setdefault("selected_option_index", -1)
    st.session_state.setdefault("replay_count", 0)
    st.session_state.setdefault("celebrated", False)


def start_round():
    st.session_state.round = build_round(st.session_state.lang, st.session_state.topic, 10)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.last_message = ""
    st.session_state.last_type = ""
    st.session_state.last_spoken_index = -1
    st.session_state.feedback_spoken_index = -1
    st.session_state.answer_locked = False
    st.session_state.selected_option_index = -1
    st.session_state.replay_count = 0
    st.session_state.celebrated = False
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
        st.session_state.lang = "vi" if st.button("🇻🇳 Tiếng Việt", use_container_width=True) else st.session_state.lang
    with col2:
        st.session_state.lang = "en" if st.button("🇺🇸 English", use_container_width=True) else st.session_state.lang

    lang = st.session_state.lang
    t = LANG[lang]
    st.subheader(f"1) {t['topic']}")
    topic_keys = list(TOPIC_META.keys())
    labels = [topic_label(k, lang) for k in topic_keys]
    selected = st.radio(
        label=t["topic"],
        options=topic_keys,
        format_func=lambda x: labels[topic_keys.index(x)],
        horizontal=False,
    )
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

    # Top header: Progress + Score + Replay Button
    c1, c2, c3 = st.columns([1.5, 1, 1])
    with c1:
        st.markdown(f"**🏅 {t['score']}: {st.session_state.score}**")
    with c2:
        st.markdown(f"**🎯 {current}/10**")
    with c3:
        if st.button("🔁 " + t["replay_audio"], use_container_width=True):
            speak(q["prompt"], lang, st.session_state.sound)
            # Force fresh choices and allow user to try again
            st.session_state.answer_locked = False
            st.session_state.selected_option_index = -1
            st.session_state.last_message = ""
            st.session_state.last_type = ""
            st.session_state.replay_count += 1
            st.session_state.feedback_spoken_index = -1
            st.rerun()

    st.progress(current / 10)
    st.markdown(f"<h3 style='text-align: center; margin-top: -10px;'>{q['prompt']}</h3>", unsafe_allow_html=True)

    if st.session_state.last_spoken_index != st.session_state.index:
        speak(q["prompt"], lang, st.session_state.sound)
        st.session_state.last_spoken_index = st.session_state.index

    # ── Image choice grid ──────────────────────────────────────────────────
    if st.session_state.answer_locked:
        # POST-ANSWER: show 2×2 grid with green/red border feedback via HTML
        grid_html = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; padding: 4px;">'
        for i in range(len(q["options"])):
            opt_label = q["options"][i]
            img_path = q["option_images"][i]
            selected = st.session_state.selected_option_index == i
            is_correct = opt_label == q["correct"]
            if selected and is_correct:
                border, bg = "6px solid #22C55E", "#F0FDF4"
            elif selected:
                border, bg = "6px solid #EF4444", "#FEF2F2"
            elif is_correct:
                border, bg = "6px solid #22C55E", "#F0FDF4"
            else:
                border, bg = "6px solid #E5E7EB", "#FFFFFF"
            
            b64_uri = to_data_uri(img_path)
            grid_html += f'''
            <div style="border:{border}; border-radius:18px; background:{bg}; padding:4px; box-shadow:0 4px 14px rgba(0,0,0,0.10);">
                <img src="{b64_uri}" style="width:100%; border-radius:14px; display:block;">
            </div>
            '''
        grid_html += '</div>'
        st.markdown(grid_html, unsafe_allow_html=True)
    else:
        # PRE-ANSWER: images are directly clickable via streamlit-clickable-images
        if clickable_images is not None:
            image_uris = [to_data_uri(p) for p in q["option_images"]]
            selected_idx = clickable_images(
                image_uris,
                titles=[""] * 4,
                div_style={
                    "display": "grid",
                    "grid-template-columns": "1fr 1fr",
                    "gap": "14px",
                    "padding": "4px",
                },
                img_style={
                    "width": "100%",
                    "border-radius": "16px",
                    "cursor": "pointer",
                    "border": "4px solid #D1D5DB",
                    "box-shadow": "0 4px 14px rgba(0,0,0,0.10)",
                    "transition": "transform 0.12s ease, box-shadow 0.12s ease",
                },
                key=f"img_click_{st.session_state.index}_{st.session_state.replay_count}",
            )
            if selected_idx > -1:
                st.session_state.selected_option_index = selected_idx
                st.session_state.answer_locked = True
                opt_label = q["options"][selected_idx]
                if opt_label == q["correct"]:
                    st.session_state.score += 1
                    st.session_state.last_message = random.choice(t["correct"])
                    st.session_state.last_type = "success"
                else:
                    st.session_state.last_message = (
                        f"{random.choice(t['wrong'])} ({q['correct']})"
                    )
                    st.session_state.last_type = "warning"
                st.rerun()
        else:
            # Safe fallback — st.button + st.image (no auto-selection possible)
            col_pairs = [st.columns(2) for _ in range(2)]
            for i in range(len(q["options"])):
                opt_label = q["options"][i]
                img_path = q["option_images"][i]
                with col_pairs[i // 2][i % 2]:
                    st.image(img_path, use_container_width=True)
                    if st.button(
                        "👆 Chọn" if lang == "vi" else "👆 Choose",
                        key=f"choice_{st.session_state.index}_{i}",
                        use_container_width=True,
                    ):
                        st.session_state.selected_option_index = i
                        st.session_state.answer_locked = True
                        if opt_label == q["correct"]:
                            st.session_state.score += 1
                            st.session_state.last_message = random.choice(t["correct"])
                            st.session_state.last_type = "success"
                        else:
                            st.session_state.last_message = (
                                f"{random.choice(t['wrong'])} ({q['correct']})"
                            )
                            st.session_state.last_type = "warning"
                        st.rerun()

    # ── Feedback & next button ──────────────────────────────────────────────
    if st.session_state.last_message:
        if st.session_state.feedback_spoken_index != st.session_state.index:
            speak(st.session_state.last_message, lang, st.session_state.sound)
            st.session_state.feedback_spoken_index = st.session_state.index
        if st.session_state.last_type == "success":
            st.success("🎉 " + st.session_state.last_message)
        else:
            st.warning("💪 " + st.session_state.last_message)

    if st.session_state.answer_locked:
        if st.button("➡️ " + t["next_question"], use_container_width=True, type="primary"):
            st.session_state.last_message = ""
            st.session_state.last_type = ""
            st.session_state.feedback_spoken_index = -1
            st.session_state.index += 1
            st.session_state.answer_locked = False
            st.session_state.selected_option_index = -1
            st.session_state.replay_count = 0  # reset for next question
            if st.session_state.index >= len(st.session_state.round):
                st.session_state.screen = "result"
            st.rerun()

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

    if not st.session_state.get("celebrated", False):
        st.balloons()
        render_fireworks()
        st.session_state.celebrated = True

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
    st.set_page_config(page_title="Học Cùng Con", page_icon="🌈", layout="centered")
    render_bgm()
    st.markdown(
        """
        <style>
            /* Reduce Streamlit container padding for mobile */
            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 1.5rem;
            }
            /* General buttons */
            .stButton button {
                height: 52px;
                font-size: 1.05rem;
                border-radius: 14px;
                font-weight: 600;
            }
            /* Choice buttons (👆 Chọn) — make them friendly and large */
            div[data-testid="stButton"] button[kind="secondary"] {
                background: linear-gradient(135deg, #6EE7F7 0%, #60A5FA 100%);
                color: #1e3a5f;
                border: none;
                height: 52px;
                font-size: 1.1rem;
                border-radius: 0 0 14px 14px;
                margin-top: 0px;
            }
            div[data-testid="stButton"] button[kind="secondary"]:hover {
                background: linear-gradient(135deg, #38BDF8 0%, #3B82F6 100%);
                transform: scale(1.03);
                transition: 0.15s ease;
            }
            /* Primary Next button */
            .stButton button[kind="primary"] {
                background: linear-gradient(135deg, #F59E0B 0%, #EF4444 100%);
                color: white;
                font-size: 1.15rem;
                height: 58px;
            }
            /* Images */
            div[data-testid="stImage"] img {
                border-radius: 14px;
                display: block;
            }
            @media (max-width: 768px) {
                .stButton button { height: 56px; font-size: 1.05rem; }
                h3 { font-size: 1.3rem !important; }
            }
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
