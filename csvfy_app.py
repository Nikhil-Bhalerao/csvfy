import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="CSVFY", page_icon=":snowflake:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_i4bqu8fz.json")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("CSVFY :wave:")
    st.write('''This Is A Free Program That Lets You View Your  Files In Better Way :tada: ''')


# file viewing section
with st.container():
    try:
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
    except ConnectionError as c:
        st.write("Faild To Connect!")
    except Exception as e:
        st.write("something went wrong!")
    else:
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.markdown('**Data From The File**')
            st.write(df)

with st.container():
    st.write("---")
    st_lottie(lottie_coding, height=300, key="coding")