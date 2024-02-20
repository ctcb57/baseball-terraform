import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import pandas as pd 
import requests
import time

st.markdown("# Batters Page")
st.sidebar.markdown("# Batting Data")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

baseball_lottie = "https://lottie.host/65150603-5c02-43e2-a583-21d8e5abeabf/LjBAz4Eadu.json"
baseball_download = load_lottieurl(baseball_lottie)

if st.button("Download"):
    with st_lottie_spinner(baseball_download, key="download"):
        time.sleep(5)
    st.balloons()