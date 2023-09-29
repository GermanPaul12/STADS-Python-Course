import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Resources for the Python course 🐍',page_icon='✔️')

st.title("Resources for the Python course 🐍")
st.write("----------")
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

with st.container():
    st.header("Links and Recommendations")
    st.markdown(read_markdown_file("General/links.md"), unsafe_allow_html=True)    
    st.write("----------")   

with st.container():
    st.header("Installation Tutorial")
    st.markdown(read_markdown_file("General/Software/installation_tutorial.md"), unsafe_allow_html=True) 
    st.write("----------")
    
with st.container():
    st.header("Installation videos")
    st.subheader("Installation video for Windows")
    st.video("https://www.youtube.com/watch?v=tDLO9hE0k-g&t=24s")
    st.subheader("Installation video for Mac")
    st.video("https://www.youtube.com/watch?v=bSMtrJlDZc4&t=106s")
    st.write("----------")         