import streamlit as st
import streamlit.components.v1 as components

# idea & html/css code from
# https://codepen.io/Hyperplexed/pen/zYWdYoo

# adjusted for streamlit by TomJohn :-)

# ------------------------------------------------------------
#
#                  Visual settings and functions
#
# ------------------------------------------------------------

# -------------- app config ---------------

st.set_page_config(page_title="German Paul CV", page_icon="📝")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------- CSS ----------------

local_css("style.css")

# ------------------------------------------------------------
#
#                        front-end
#
# ------------------------------------------------------------

f = open("cards.txt")

st.markdown(str(f.read()), unsafe_allow_html=True)

f.close()
