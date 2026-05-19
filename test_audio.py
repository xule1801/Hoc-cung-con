import streamlit as st
st.title("Test Audio Rerun")
if "count" not in st.session_state: st.session_state.count = 0
st.button("Click Me", on_click=lambda: st.session_state.update(count=st.session_state.count+1))
st.write("Count:", st.session_state.count)
st.markdown('<audio autoplay loop><source src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3" type="audio/mpeg"></audio>', unsafe_allow_html=True)
