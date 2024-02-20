import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import pandas as pd 
import requests
import time


title_col1, title_col2, title_col3 = st.columns([1, 5, 1])
title_col2.header('Pitching', divider='red')

if 'pitcher_id' not in st.session_state:
    st.session_state.pitcher_id = ''

with st.form("pitcher_search"):
    pitcher_name = st.text_input(
        "Enter a pitchers name 👇", 
        key="pitcher_id"
    )
    st.form_submit_button('Submit Name')

# with st.form('pitchers'):


# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None 
#     return r.json()

# baseball_lottie = "https://lottie.host/2070d1cd-8770-4b48-b8f5-1464d121b01e/kD0vaK3j32.json"
# baseball_download = load_lottieurl(baseball_lottie)

# if st.button("Download"):
#     with st_lottie_spinner(baseball_download, key="download"):
#         time.sleep(5)
#     st.balloons()