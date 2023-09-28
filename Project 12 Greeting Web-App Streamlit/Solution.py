import streamlit as st

st.title("My Greeting Web Application")
name = st.text_input("Enter your name here")
if name:
    st.success(f"Hello {name}!")
    
st.write("Click me for the streamlit documentation [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")    