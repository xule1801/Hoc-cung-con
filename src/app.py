import random
import base64
import mimetypes
import json
import os
import html
import urllib.error
import urllib.request
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
from icons_config import ICONS
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


def render_bgm(enabled: bool = True):
    bgm_path = AUDIO_DIR / "bgm.mp3"
    if not enabled:
        st.components.v1.html(
            """
            <script>
                var audio = window.parent.document.getElementById("my-bgm");
                if (audio) { audio.pause(); }
            </script>
            """,
            width=0,
            height=0,
        )
        return
    if not bgm_path.exists():
        return
    b64 = base64.b64encode(bgm_path.read_bytes()).decode()
    html_str = f"""
    <script>
        var parentDoc = window.parent.document;
        var audio = parentDoc.getElementById("my-bgm");
        if (!audio) {{
            audio = parentDoc.createElement("audio");
            audio.id = "my-bgm";
            audio.src = "data:audio/mp3;base64,{b64}";
            audio.loop = true;
            parentDoc.body.appendChild(audio);
        }}
        audio.volume = 0.18;
        var playPromise = audio.play();
        if (playPromise !== undefined) {{
            playPromise.catch(function(error) {{
                parentDoc.addEventListener("click", function() {{
                    audio.play();
                }}, {{once: true}});
            }});
        }}
    </script>
    """
    st.components.v1.html(html_str, width=0, height=0)


def render_fireworks():
    applause_path = AUDIO_DIR / "applause.ogg"
    applause_mime = "audio/ogg"
    if not applause_path.exists():
        applause_path = AUDIO_DIR / "applause.mp3"
        applause_mime = "audio/mpeg"
    audio_js = ""
    if applause_path.exists():
        b64 = base64.b64encode(applause_path.read_bytes()).decode()
        audio_js = f"""
        var parentDoc = window.parent.document;
        var oldAudio = parentDoc.getElementById("completion-applause");
        if (oldAudio) {{ oldAudio.pause(); oldAudio.remove(); }}
        var audio = parentDoc.createElement("audio");
        audio.id = "completion-applause";
        audio.src = "data:{applause_mime};base64,{b64}";
        audio.volume = 0.9;
        audio.loop = true;
        parentDoc.body.appendChild(audio);
        var playPromise = audio.play();
        if (playPromise !== undefined) {{
            playPromise.catch(function(e) {{ console.log(e); }});
        }}
        setTimeout(function() {{ audio.pause(); audio.remove(); }}, 10000);
        """
        
    html_str = f"""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
      {audio_js}
      var duration = 10 * 1000;
      var end = Date.now() + duration;
      (function frame() {{
        confetti({{ particleCount: 5, angle: 60, spread: 55, origin: {{ x: 0 }}, colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00'] }});
        confetti({{ particleCount: 5, angle: 120, spread: 55, origin: {{ x: 1 }}, colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00'] }});
        if (Date.now() < end) {{ requestAnimationFrame(frame); }}
      }}());
    </script>
    """
    st.components.v1.html(html_str, width=0, height=0)


def stop_applause():
    st.components.v1.html(
        """
        <script>
            var audio = window.parent.document.getElementById("completion-applause");
            if (audio) {
                audio.pause();
                audio.remove();
            }
        </script>
        """,
        width=0,
        height=0,
    )


def get_config_value(name: str, default: str = "") -> str:
    value = os.getenv(name)
    if value:
        return value
    try:
        value = st.secrets.get(name, default)
    except Exception:
        value = default
    return str(value) if value else default


def azure_voice(lang: str) -> str:
    if lang == "vi":
        return get_config_value("AZURE_SPEECH_VOICE_VI", "vi-VN-HoaiMyNeural")
    return get_config_value("AZURE_SPEECH_VOICE_EN", "en-US-JennyNeural")


@st.cache_data(show_spinner=False, ttl=86400)
def azure_tts_data_uri(text: str, lang: str):
    key = get_config_value("AZURE_SPEECH_KEY")
    region = get_config_value("AZURE_SPEECH_REGION")
    if not key or not region:
        return None

    voice = azure_voice(lang)
    language = "vi-VN" if lang == "vi" else "en-US"
    ssml_text = html.escape(text, quote=True)
    ssml = f"""
    <speak version="1.0" xml:lang="{language}">
      <voice xml:lang="{language}" name="{voice}">{ssml_text}</voice>
    </speak>
    """.strip()
    request = urllib.request.Request(
        f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1",
        data=ssml.encode("utf-8"),
        headers={
            "Ocp-Apim-Subscription-Key": key,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",
            "User-Agent": "hoc-cung-con-streamlit",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            audio_bytes = response.read()
    except (urllib.error.URLError, TimeoutError, ValueError):
        return None
    encoded = base64.b64encode(audio_bytes).decode("utf-8")
    return f"data:audio/mpeg;base64,{encoded}"


def render_speech_button(*_args, **_kwargs) -> None:
    return


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
    audio_src = azure_tts_data_uri(text, lang)
    if not audio_src:
        return
    audio_src_json = json.dumps(audio_src)
    components.html(
        f"""
        <audio id="tts-audio" src={audio_src_json} autoplay playsinline></audio>
        <script>
            const audio = document.getElementById("tts-audio");
            audio.volume = 1;
            const p = audio.play();
            if (p !== undefined) {{
                p.catch(function() {{}});
            }}
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
    if "bgm_enabled" not in st.session_state:
        st.session_state.bgm_enabled = st.session_state.get("sound", True)
    st.session_state.setdefault("round", [])
    st.session_state.setdefault("index", 0)
    st.session_state.setdefault("score", 0)
    st.session_state.setdefault("last_message", "")
    st.session_state.setdefault("last_audio_message", "")
    st.session_state.setdefault("last_type", "")
    st.session_state.setdefault("last_spoken_index", -1)
    st.session_state.setdefault("feedback_spoken_index", -1)
    st.session_state.setdefault("answer_locked", False)
    st.session_state.setdefault("selected_option_index", -1)
    st.session_state.setdefault("question_had_wrong_attempt", False)
    st.session_state.setdefault("question_scored", False)
    st.session_state.setdefault("pending_score_increment", 0)
    st.session_state.setdefault("replay_count", 0)
    st.session_state.setdefault("celebrated", False)


def start_round():
    st.session_state.round = build_round(st.session_state.lang, st.session_state.topic, 10)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.last_message = ""
    st.session_state.last_audio_message = ""
    st.session_state.last_type = ""
    st.session_state.last_spoken_index = -1
    st.session_state.feedback_spoken_index = -1
    st.session_state.answer_locked = False
    st.session_state.selected_option_index = -1
    st.session_state.question_had_wrong_attempt = False
    st.session_state.question_scored = False
    st.session_state.pending_score_increment = 0
    st.session_state.replay_count = 0
    st.session_state.celebrated = False
    st.session_state.screen = "quiz"


def handle_choice(selected_idx: int, q: dict, t: dict) -> None:
    opt_label = q["options"][selected_idx]
    st.session_state.selected_option_index = selected_idx
    st.session_state.answer_locked = True
    if opt_label == q["correct"]:
        if (
            not st.session_state.question_had_wrong_attempt
            and not st.session_state.question_scored
        ):
            st.session_state.pending_score_increment = 1
            st.session_state.question_scored = True
        feedback = random.choice(t["correct"])
        st.session_state.last_message = feedback
        st.session_state.last_audio_message = feedback
        st.session_state.last_type = "success"
    else:
        feedback = random.choice(t["wrong"])
        st.session_state.question_had_wrong_attempt = True
        st.session_state.last_message = f"{feedback} ({q['correct']})"
        st.session_state.last_audio_message = feedback
        st.session_state.last_type = "warning"


def grade_feedback(score: int, lang: str) -> str:
    bands = LANG[lang]["feedback_bands"]
    for limit, text in bands:
        if score <= limit:
            return text
    return bands[-1][1]


def render_parent_guide():
    lang = st.session_state.lang
    t = LANG[lang]
    st.markdown(f"<h2 class='guide-title'>📘 {t['parent_guide_title']}</h2>", unsafe_allow_html=True)
    for item in t["parent_guide_items"]:
        st.markdown(f"<p class='guide-item'>{item}</p>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🏠 " + t["home"], use_container_width=True):
            stop_applause()
            st.session_state.screen = "home"
            st.rerun()
    with c2:
        if st.button("🚀 " + t["start"], use_container_width=True):
            start_round()
            st.rerun()


def handle_query_actions():
    action = st.query_params.get("quiz_action")
    if not action:
        return
    st.query_params.clear()
    if action == "home":
        stop_applause()
        st.session_state.screen = "home"
    elif action == "sound":
        st.session_state.bgm_enabled = not st.session_state.bgm_enabled
    st.rerun()


def render_quiz_header() -> None:
    sound_icon = ICONS["sound_on"] if st.session_state.bgm_enabled else ICONS["sound_off"]
    st.markdown(
        f"""
        <nav class="quiz-header-fixed" aria-label="Quiz navigation">
            <a class="quiz-icon-link" href="?quiz_action=home" aria-label="Home">{ICONS["home"]}</a>
            <a class="quiz-icon-link" href="?quiz_action=sound" aria-label="Speaker">{sound_icon}</a>
        </nav>
        """,
        unsafe_allow_html=True,
    )


def render_home():
    lang = st.session_state.lang
    t = LANG[lang]
    st.markdown(f"<h2 class='home-title'>🌈 {t['app_name']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='home-subtitle'>{t['subtitle']}</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.lang = "vi" if st.button("🇻🇳 Tiếng Việt", use_container_width=True) else st.session_state.lang
    with col2:
        st.session_state.lang = "en" if st.button("🇺🇸 English", use_container_width=True) else st.session_state.lang

    lang = st.session_state.lang
    t = LANG[lang]
    topic_keys = list(TOPIC_META.keys())
    labels = [topic_label(k, lang) for k in topic_keys]
    selected = st.selectbox(
        label=t["topic"],
        options=topic_keys,
        format_func=lambda x: labels[topic_keys.index(x)],
    )
    st.session_state.topic = selected

    st.session_state.bgm_enabled = st.toggle("🔊 " + t["sound_on"], value=st.session_state.bgm_enabled)

    st.markdown("<div class='home-action-buttons'></div>", unsafe_allow_html=True)
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
    completed = st.session_state.index

    render_quiz_header()
    st.markdown("<div class='quiz-top-actions'></div>", unsafe_allow_html=True)

    score_label = "Số câu đúng" if lang == "vi" else "Correct answers"
    st.markdown(
        f"<div class='quiz-score'>{score_label}: {st.session_state.score}/{completed}</div>",
        unsafe_allow_html=True,
    )

    replay_label = f"{ICONS['audio_btn']} Nghe lại" if lang == "vi" else f"{ICONS['audio_btn']} Replay"
    if st.button(replay_label, key=f"replay_main_{st.session_state.index}_{st.session_state.replay_count}", use_container_width=True):
        speak(q["prompt"], lang, True)
        if st.session_state.answer_locked and st.session_state.last_type == "warning":
            st.session_state.answer_locked = False
            st.session_state.selected_option_index = -1
            st.session_state.last_message = ""
            st.session_state.last_audio_message = ""
            st.session_state.last_type = ""
            st.session_state.feedback_spoken_index = -1
            st.session_state.replay_count += 1
            st.rerun()

    st.markdown(f"<h3 class='quiz-prompt'>{q['prompt']}</h3>", unsafe_allow_html=True)

    if st.session_state.last_spoken_index != st.session_state.index:
        speak(q["prompt"], lang, True)
        st.session_state.last_spoken_index = st.session_state.index

    # ── Image choice grid ──────────────────────────────────────────────────
    if st.session_state.answer_locked:
        grid_html = """
        <style>
            body { margin: 0; padding: 0; overflow: hidden; background: transparent; }
            .answer-grid {
                width: 100%;
                box-sizing: border-box;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 12px;
                padding: 0 16px;
            }
            .answer-card {
                border-radius: 12px;
                padding: 3px;
                box-shadow: 0 6px 10px rgba(0,0,0,0.08);
                box-sizing: border-box;
            }
            .answer-card img {
                width: 100%;
                height: clamp(100px, 40dvh, 168px);
                object-fit: contain;
                border-radius: 8px;
                display: block;
            }
        </style>
        <div class="answer-grid">
        """
        for i in range(len(q["options"])):
            opt_label = q["options"][i]
            img_path = q["option_images"][i]
            selected = st.session_state.selected_option_index == i
            is_correct = opt_label == q["correct"]
            if selected and is_correct:
                border, bg = "3px solid #22C55E", "#F0FFF4"
            elif selected:
                border, bg = "3px solid #EF4444", "#FFF5F5"
            elif is_correct:
                border, bg = "3px solid #22C55E", "#F0FFF4"
            else:
                border, bg = "1.5px solid #E5E7EB", "#FFFFFF"
            
            b64_uri = to_data_uri(img_path)
            grid_html += f'''
            <div class="answer-card" style="border:{border}; background:{bg};">
                <img src="{b64_uri}">
            </div>
            '''
        grid_html += "</div>"
        components.html(grid_html, height=380, scrolling=False)
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
                    "gap": "12px",
                    "padding": "0 16px",
                },
                img_style={
                    "height": "clamp(96px, 17dvh, 156px)",
                    "width": "100%",
                    "border-radius": "16px",
                    "cursor": "pointer",
                    "border": "1.5px solid #E5E7EB",
                    "box-shadow": "0 5px 12px rgba(0,0,0,0.08)",
                    "object-fit": "contain",
                    "background": "#FFFFFF",
                    "transition": "transform 0.12s ease, box-shadow 0.12s ease",
                },
                key=f"img_click_{st.session_state.index}_{st.session_state.replay_count}",
            )
            if selected_idx > -1:
                handle_choice(selected_idx, q, t)
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
                        handle_choice(i, q, t)
                        st.rerun()

    # ── Feedback & next button ──────────────────────────────────────────────
    if st.session_state.last_message:
        if st.session_state.feedback_spoken_index != st.session_state.index:
            speak(st.session_state.last_audio_message or st.session_state.last_message, lang, True)
            st.session_state.feedback_spoken_index = st.session_state.index

    if st.session_state.answer_locked:
        next_label = "TIẾP THEO ➤" if lang == "vi" else "NEXT ➤"
        st.markdown("<div class='quiz-footer-action'></div>", unsafe_allow_html=True)
        if st.button(next_label, key=f"next_{st.session_state.index}", type="primary", use_container_width=True):
            st.session_state.score += st.session_state.pending_score_increment
            st.session_state.pending_score_increment = 0
            st.session_state.last_message = ""
            st.session_state.last_audio_message = ""
            st.session_state.last_type = ""
            st.session_state.feedback_spoken_index = -1
            st.session_state.index += 1
            st.session_state.answer_locked = False
            st.session_state.selected_option_index = -1
            st.session_state.question_had_wrong_attempt = False
            st.session_state.question_scored = False
            st.session_state.pending_score_increment = 0
            st.session_state.replay_count = 0
            if st.session_state.index >= len(st.session_state.round):
                st.session_state.screen = "result"
            st.rerun()


def render_result():
    lang = st.session_state.lang
    t = LANG[lang]
    score = st.session_state.score
    wrong = 10 - score

    st.markdown(f"<h2 class='result-title'>🏁 {t['result']}</h2>", unsafe_allow_html=True)
    st.markdown(
        (
            "<div class='result-stats'>"
            f"<div><strong>{t['total']}:</strong> 10</div>"
            f"<div><strong>{t['right']}:</strong> {score}</div>"
            f"<div><strong>{t['wrong_count']}:</strong> {wrong}</div>"
            f"<div><strong>{t['score']}:</strong> {score}/10</div>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )
    st.markdown(f"<div class='result-feedback'>{grade_feedback(score, lang)}</div>", unsafe_allow_html=True)

    if not st.session_state.get("celebrated", False):
        st.balloons()
        render_fireworks()
        st.session_state.celebrated = True

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🔁 " + t["play_again"], use_container_width=True):
            stop_applause()
            start_round()
            st.rerun()
    with c2:
        if st.button("🧩 " + t["change_topic"], use_container_width=True):
            stop_applause()
            st.session_state.screen = "home"
            st.rerun()
    with c3:
        if st.button("🏠 " + t["home"], use_container_width=True):
            stop_applause()
            st.session_state.screen = "home"
            st.rerun()


def main():
    st.set_page_config(page_title="Học Cùng Con", page_icon="🌈", layout="centered")
    init_state()
    handle_query_actions()
    render_bgm(st.session_state.bgm_enabled)
    st.markdown(
        """
        <style>
            header[data-testid="stHeader"], #MainMenu, footer {
                visibility: hidden;
                height: 0;
            }
            .stApp {
                background-color: #FAF9F6;
                overflow-x: hidden !important;
            }
            html, body {
                overflow: hidden !important;
                height: 100dvh !important;
                max-height: 100dvh !important;
            }
            [data-testid="stAppViewContainer"], .main {
                overflow: hidden !important;
                max-width: 100vw !important;
                height: 100dvh !important;
            }
            :root {
                --space-1: 4px;
                --space-2: 8px;
                --space-3: 12px;
                --space-4: 16px;
                --radius-sm: 8px;
                --radius-md: 12px;
                --radius-lg: 16px;
                --font-xs: clamp(0.82rem, 3vw, 0.9rem);
                --font-sm: clamp(0.9rem, 3.2vw, 1rem);
                --font-md: clamp(1rem, 3.8vw, 1.1rem);
                --font-lg: clamp(1.2rem, 4.5vw, 1.7rem);
            }
            .main .block-container {
                max-width: 100% !important;
                padding: max(env(safe-area-inset-top), 6px) max(env(safe-area-inset-right), 6px) max(env(safe-area-inset-bottom), 6px) max(env(safe-area-inset-left), 6px) !important;
                height: 100dvh !important;
                min-height: 100dvh !important;
                overflow: hidden !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: space-between !important;
            }
            div[data-testid="stVerticalBlock"] {
                gap: var(--space-2);
            }
            .quiz-score {
                color: #2ECC71;
                font-size: var(--font-md);
                font-weight: 700;
                line-height: 1.1;
                margin: 0;
                padding: 0 var(--space-4);
            }
            .home-title {
                text-align: center;
                margin: 0.2rem 0 0.1rem 0 !important;
                line-height: 1.1;
                font-size: clamp(1.35rem, 5vw, 1.9rem) !important;
            }
            .home-subtitle {
                text-align: center;
                margin: 0 0 var(--space-2) 0;
                color: #4b5563;
                font-size: var(--font-xs);
                line-height: 1.3;
            }
            .guide-title, .result-title {
                margin: 0.2rem 0 0.3rem 0 !important;
                text-align: center;
                line-height: 1.15;
                font-size: var(--font-lg) !important;
                color: #1f2937;
            }
            .guide-item {
                margin: 0;
                font-size: var(--font-sm);
                line-height: 1.32;
                color: #374151;
            }
            .result-stats {
                background: #ffffff;
                border: 1.5px solid #f59e0b;
                border-radius: var(--radius-md);
                padding: 10px 12px;
                display: grid;
                gap: 6px;
                color: #1f2937;
                font-size: var(--font-sm);
            }
            .result-feedback {
                margin-top: 0.35rem;
                border-radius: var(--radius-sm);
                background: #ecfeff;
                border: 1px solid #67e8f9;
                color: #155e75;
                padding: 8px 10px;
                font-size: var(--font-sm);
                line-height: 1.35;
            }
            .home-action-buttons + div[data-testid="stHorizontalBlock"] button {
                min-height: 62px;
                border-radius: 16px;
                border: 1.5px solid #f59e0b;
                background: linear-gradient(180deg, #fff7d6 0%, #fde68a 100%);
                color: #92400e;
                font-size: clamp(0.95rem, 3.3vw, 1.1rem);
                font-weight: 800;
                box-shadow: 0 6px 12px rgba(146, 64, 14, 0.12);
                transform: translateY(0);
                transition: transform 0.12s ease, box-shadow 0.12s ease;
            }
            .home-action-buttons + div[data-testid="stHorizontalBlock"] button:hover {
                border-color: #d97706;
                transform: translateY(1px);
                box-shadow: 0 4px 8px rgba(146, 64, 14, 0.1);
            }
            .quiz-prompt {
                text-align: center;
                margin: 0.35rem 0 0.2rem 0 !important;
                line-height: 1.15;
                font-size: var(--font-md) !important;
                color: #333333;
            }
            .answer-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: var(--space-3);
                padding: 0 var(--space-4);
            }
            .answer-card {
                border-radius: var(--radius-md);
                padding: 3px;
                box-shadow: 0 6px 10px rgba(0,0,0,0.08);
                min-height: 0;
            }
            .answer-card img {
                width: 100%;
                height: clamp(96px, 17dvh, 156px);
                object-fit: contain;
                border-radius: var(--radius-sm);
                display: block;
            }
            .audio-feedback {
                text-align: center;
                font-size: clamp(1.6rem, 5vw, 2.4rem);
                line-height: 1;
                height: 3.2rem;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0.3rem 0 0.45rem 0;
                overflow: visible;
            }
            /* General buttons */
            .stButton button {
                height: 44px;
                font-size: var(--font-sm);
                border-radius: var(--radius-md);
                font-weight: 600;
            }
            div[data-testid="stSelectbox"] > div,
            div[data-testid="stSelectbox"] label,
            div[data-testid="stSelectbox"] [data-baseweb="select"] {
                font-size: clamp(0.9rem, 3.3vw, 1rem);
            }
            div[data-testid="stSelectbox"] [data-baseweb="select"] {
                min-height: 44px;
            }
            div[data-testid="stToggle"] label p {
                font-size: var(--font-sm) !important;
                font-weight: 600;
            }
            div[data-testid="stButton"] button[kind="secondary"] {
                background: transparent;
                border: none;
                color: #1f2937;
                box-shadow: none;
            }
            /* Icon buttons — broad selectors survive Streamlit DOM changes */
            button[aria-label="Trang chủ"],
            button[aria-label="Home"],
            div[data-testid="stButton"] button[aria-label="Trang chủ"],
            div[data-testid="stButton"] button[aria-label="Home"] {
                height: 56px !important;
                width: 150px !important;
                border-radius: 8px !important;
                font-size: 1.35rem !important;
                font-weight: 800 !important;
                background: #0678C9 !important;
                color: #FFFFFF !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 18px !important;
            }
            button[aria-label="🔊"],
            button[aria-label="🔇"],
            div[data-testid="stButton"] button[aria-label="🔊"],
            div[data-testid="stButton"] button[aria-label="🔇"] {
                height: 56px !important;
                border-radius: 0 !important;
                font-size: 2rem !important;
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
            }
            .quiz-top-actions {
                height: 72px;
                width: 100%;
            }
            .quiz-header-fixed {
                position: fixed !important;
                top: calc(max(env(safe-area-inset-top), 0px) + 16px) !important;
                left: 0 !important;
                right: 0 !important;
                z-index: 10000 !important;
                width: 100vw !important;
                height: 48px !important;
                padding: 0 20px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: space-between !important;
                box-sizing: border-box !important;
                pointer-events: none;
            }
            .quiz-icon-link {
                width: 48px !important;
                height: 48px !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                border-radius: 12px !important;
                color: #111827 !important;
                text-decoration: none !important;
                font-size: 2rem !important;
                line-height: 1 !important;
                pointer-events: auto;
            }
            button[aria-label^="🎧"],
            div[data-testid="stButton"] button[aria-label^="🎧"] {
                background: linear-gradient(90deg, #5B9BD5 0%, #4A7FC1 100%) !important;
                color: #FFF1C2 !important;
                border: none !important;
                height: 64px !important;
                font-size: 1.2rem !important;
                border-radius: 12px !important;
                box-shadow: none !important;
                margin: 0 0 0.45rem 0;
            }
            div[data-testid="stButton"]:has(button[aria-label="⁣"]),
            div[data-testid="stButton"] button[aria-label="⁣"] {
                display: none;
            }
            div[data-testid="stButton"] button[kind="secondary"]:hover {
                border: none;
            }
            /* Primary Next button — broad selectors */
            button[data-testid="baseButton-primary"],
            .stButton button[kind="primary"],
            button[kind="primary"] {
                background: #EF4444 !important;
                color: #FFFFFF !important;
                font-size: 2rem !important;
                font-weight: 800 !important;
                line-height: 1 !important;
                height: 64px !important;
                border-radius: 14px !important;
                padding: 0 !important;
                border: none !important;
                box-shadow: none !important;
            }
            /* Images */
            div[data-testid="stImage"] img {
                border-radius: 14px;
                display: block;
            }
            iframe {
                max-width: 100% !important;
                width: 100% !important;
            }
            .stApp,
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(180deg, #FFFFFF 0%, #F7F8FA 42%, #D1D5DB 100%) !important;
            }
            .main .block-container {
                padding-top: calc(max(env(safe-area-inset-top), 0px) + 18px) !important;
                padding-bottom: calc(max(env(safe-area-inset-bottom), 0px) + 22px) !important;
            }
            button[aria-label="🏠"],
            div[data-testid="stButton"] button[aria-label="🏠"] {
                width: 48px !important;
                height: 48px !important;
                min-height: 48px !important;
                border-radius: 12px !important;
                background: transparent !important;
                color: #111827 !important;
                border: none !important;
                box-shadow: none !important;
                font-size: 2rem !important;
                line-height: 1 !important;
                padding: 0 !important;
            }
            button[aria-label="🔊"],
            button[aria-label="🔇"],
            div[data-testid="stButton"] button[aria-label="🔊"],
            div[data-testid="stButton"] button[aria-label="🔇"] {
                width: 48px !important;
                height: 48px !important;
                min-height: 48px !important;
                border-radius: 12px !important;
                color: #111827 !important;
                font-size: 2rem !important;
                line-height: 1 !important;
            }
            .quiz-top-actions {
                height: 72px !important;
            }
            .quiz-footer-action {
                height: 64px;
            }
            div[data-testid="stElementContainer"]:has(.quiz-footer-action) + div[data-testid="stButton"] {
                position: fixed !important;
                right: max(env(safe-area-inset-right), 20px) !important;
                bottom: calc(max(env(safe-area-inset-bottom), 0px) + 46px) !important;
                width: min(176px, calc(100vw - 40px)) !important;
                z-index: 10000 !important;
            }
            div[data-testid="stElementContainer"]:has(.quiz-footer-action) + div[data-testid="stButton"] button[kind="primary"],
            div[data-testid="stElementContainer"]:has(.quiz-footer-action) + div[data-testid="stButton"] button[data-testid="baseButton-primary"] {
                height: 52px !important;
                min-height: 52px !important;
                border-radius: 12px !important;
                background: #2563EB !important;
                color: #FFFFFF !important;
                font-size: 0.95rem !important;
                font-weight: 800 !important;
                letter-spacing: 0 !important;
                padding: 0 18px !important;
                border: none !important;
                box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3) !important;
                white-space: nowrap !important;
            }
            @media (max-width: 768px) {
                .block-container {
                    padding-top: env(safe-area-inset-top);
                    padding-bottom: env(safe-area-inset-bottom);
                }
                div[data-testid="stVerticalBlock"] {
                    gap: 0.4rem;
                }
                button[data-testid="baseButton-primary"],
                .stButton button[kind="primary"] {
                    height: 56px !important;
                    font-size: 1.8rem !important;
                }
                button[aria-label="🔊"],
                button[aria-label="🔇"] {
                    height: 56px !important;
                    font-size: 2rem !important;
                }
                button[aria-label^="🎧"],
                div[data-testid="stButton"] button[aria-label^="🎧"] {
                    height: 60px !important;
                    font-size: 1.1rem;
                    margin-bottom: 0.35rem;
                }
                .quiz-score {
                    font-size: 1rem;
                }
                .home-title {
                    font-size: 1.5rem !important;
                }
                .guide-title, .result-title {
                    font-size: 1.35rem !important;
                }
                .home-subtitle {
                    font-size: 0.84rem;
                    margin-bottom: 0.3rem;
                }
                .guide-item,
                .result-stats,
                .result-feedback {
                    font-size: 0.9rem;
                }
                .home-action-buttons + div[data-testid="stHorizontalBlock"] button {
                    min-height: 58px;
                    font-size: 0.95rem;
                }
                .quiz-prompt {
                    font-size: 1rem !important;
                    margin: 0.25rem 0 0.2rem 0 !important;
                }
                .answer-grid {
                    gap: 12px;
                }
                .answer-card {
                    border-radius: 12px;
                    padding: 3px;
                }
                .answer-card img {
                    height: clamp(96px, 17dvh, 146px);
                    border-radius: 8px;
                }
            }
            @media (max-height: 700px) {
                .home-subtitle {
                    display: none;
                }
                .guide-title, .result-title {
                    font-size: 1.15rem !important;
                    margin-bottom: 0.2rem !important;
                }
                .guide-item,
                .result-stats,
                .result-feedback {
                    font-size: 0.84rem;
                    line-height: 1.25;
                }
                .home-action-buttons + div[data-testid="stHorizontalBlock"] button {
                    min-height: 52px;
                }
                button[data-testid="baseButton-primary"],
                .stButton button[kind="primary"] {
                    height: 52px !important;
                }
                .quiz-prompt {
                    font-size: 0.95rem !important;
                }
                .answer-card img {
                    height: clamp(84px, 15dvh, 128px);
                }
                .quiz-score {
                    font-size: 0.95rem;
                }
                div[data-testid="stButton"] button[aria-label^="🎧"] {
                    height: 54px;
                    font-size: 1rem;
                }
                .audio-feedback {
                    font-size: 1.35rem;
                    height: 2.4rem;
                    margin: 0.18rem 0 0.28rem 0;
                }
            }
            /* Samsung Galaxy A73 5G ~ 412x915 CSS viewport */
            @media (min-width: 400px) and (max-width: 430px) and (min-height: 880px) and (max-height: 940px) {
                .main .block-container {
                    padding-top: max(env(safe-area-inset-top), 10px) !important;
                    padding-bottom: max(env(safe-area-inset-bottom), 10px) !important;
                }
                .home-title, .guide-title, .result-title {
                    font-size: 1.5rem !important;
                }
                .quiz-score {
                    font-size: 1.05rem;
                }
                .quiz-prompt {
                    font-size: 1.08rem !important;
                    margin: 0.35rem 0 0.25rem 0 !important;
                }
                /* Pre-answer: images in clickable_images grid (dvh = main viewport 915px)
                   18dvh × 915 = 164.7px → max 168px */
                .answer-card img {
                    height: clamp(140px, 18dvh, 168px);
                }
                div[data-testid="stButton"] button[aria-label^="🎧"] {
                    height: 64px;
                    font-size: 1.18rem;
                }
                button[data-testid="baseButton-primary"],
                .stButton button[kind="primary"] {
                    height: 58px !important;
                }
                .result-stats {
                    gap: 6px;
                }
                .guide-item, .result-feedback {
                    font-size: 0.92rem;
                }
                /* Post-answer: expand the locked-state answer grid iframe.
                   At 420px: 40dvh × 420 = 168px → matches pre-answer images. */
                div[data-testid="stCustomComponentV1"]:not([style*="height: 0"]) iframe {
                    height: 420px !important;
                    min-height: 420px !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
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
