import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from pathlib import Path
import os

# PageConfig
st.set_page_config(page_title='Homepage',page_icon='🏠')
st.sidebar.success('Select a page above ⬆')

# ---- HEADER SECTION ----
with st.container():
    st.title('Fortgeschrittene Programmierung - Webapplikation')
    st.write('You want to see our code? ➡ Check out our [Github Repository](https://github.com/GermanPaul12/Streamlit-and-Voila-Website-Fortgeschrittene-Programmierung) 💡')

# ---- MAIN SECTION ----

with st.container():
    st.write('---')
    st.header('Target Goal')
    st.write('We wanted to show how easy and fast you can build web-applications in Python only using the streamlit package. The result can be seen under 🧮:orange[Calculator] in the sidebar.')
    st.write("If you're interested how our code works you should click on 👨‍💻:orange[Code].")
    
# ---- Credits ----
with st.container():
    st.write('---')
    
    st.header('Contributers')
    #col1,col2,col3,col4 = st.columns(4)
    col1,col2 = st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
        GP_image = Image.open('assets/img/GP_Github.png')
        st.image(GP_image,use_column_width=True, caption='German Paul')
    with col2:
        MG_image = Image.open('assets/img/MG_Github.png')
        st.image(MG_image,use_column_width=True, caption='Michael Greif')
    with col3:
        DS_image = Image.open('assets/img/DS_Github.png')
        st.image(DS_image,use_column_width=True, caption='David Siregar')
    with col4:
        FM_image = Image.open('assets/img/FM_Github.png')
        st.image(FM_image,use_column_width=True, caption='Finn Münstermann')

with st.container():
    st.write('---')
    st.header('Read the docs')
    col1,col2 = st.columns(2)
    with col1:
        voila_image = Image.open("assets/img/voila_icon.png")
        st.image(voila_image,use_column_width=True)
        st.markdown("""<a style='display: block; text-align: center;' href="https://voila.readthedocs.io/en/stable/">Voila</a>""",unsafe_allow_html=True,)
    with col2:
        streamlit_image = Image.open("assets/img/streamlit_icon.png")
        st.image(streamlit_image,use_column_width=True)
        st.markdown("""<a style='display: block; text-align: center;' href="https://docs.streamlit.io/">Streamlit</a>""",unsafe_allow_html=True,)
        

   
        