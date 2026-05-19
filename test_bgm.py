import streamlit as st
import streamlit.components.v1 as components

st.title("Test BGM")

if "count" not in st.session_state:
    st.session_state.count = 0

st.button("Rerun", on_click=lambda: st.session_state.update(count=st.session_state.count+1))
st.write("Count:", st.session_state.count)

components.html("""
<audio controls autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=lullaby-112344.mp3" type="audio/mpeg">
</audio>
""", height=50)
