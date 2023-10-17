import streamlit as st
from streamlit_extras.badges import badge

# PageConfig
st.set_page_config(page_title='Homepage',page_icon='🏠')
st.sidebar.success('Select a page above ⬆')

# ---- HEADER SECTION ----
with st.container():
    st.title('Python Course - Web-App')
    st.write('You want to see the code? ➡ Check out the [Github Repository](https://github.com/GermanPaul12/STADS-Python-Course) 💡')

# ---- MAIN SECTION ----

with st.container():
    st.write('---')
    st.header('Target Goal')
    st.write('A web-app which offers a quick overview over the course and some important information. The timetable can be seen under ⏱️:blue[Schedule Planner] in the sidebar.')
    
# ---- Credits ----
with st.container():
    st.write('---')
    
    st.header('Contributers')
    #col1,col2,col3,col4 = st.columns(4)
    col1,col2 = st.columns(2)
    
    with col1:
        GP_image = 'https://raw.githubusercontent.com/GermanPaul12/Streamlit-and-Voila-Website-Fortgeschrittene-Programmierung/master/assets/img/GP_Github.png'
        st.image(GP_image,use_column_width=True, caption='German Paul')
    with col2:
        pass
    
with st.container():
    st.write('---')
    
    st.header('Social Media')
    #col1,col2,col3,col4 = st.columns(4)
    col1,col2 = st.columns(2)
    
    with col1:
        badge(type="github", name="GermanPaul12")

    with col2:
        st.markdown("[![Foo](https://github.com/GermanPaul12/STADS-Python-Course/blob/main/Streamlit/assets/linkedin.png?raw=True)](https://www.linkedin.com/in/germanpaul12/)")


''' [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/GermanPaul12/STADS-Python-Course) '''         
st.markdown("<br>",unsafe_allow_html=True)