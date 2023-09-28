import streamlit as st
import datetime as dt
from pathlib import Path
import os

st.set_page_config(page_title='Schedule Planner',page_icon='⏱️')
st.title("Schedule Planner")


#for i in range(1,9):
#    with open(f"/Users/german/Documents/STADS/STADS-Python-Course/Project 9 Web-App Streamlit/Schedule Plan Python Course/assets/week_{i}.md", "r+") as f:
#        pass


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

content = [read_markdown_file(f"{os.getcwd()}/assets/week_{i}.md") for i in range(1,9)]


time_comparison = dt.datetime.strptime("2023-09-21", "%Y-%m-%d")
st.write("----")
for i in range(1,9):
    if dt.datetime.now() >= time_comparison:
        st.header(f":blue[Week {i}]")
        st.markdown(content[i-1], unsafe_allow_html=True)
        st.write("----")
        time_comparison += dt.timedelta(days=7)
