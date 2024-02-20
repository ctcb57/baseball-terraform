import streamlit as st
from streamlit_lottie import st_lottie
from google.oauth2 import service_account
from google.cloud import bigquery
import numpy as np
import pandas as pd
from PIL import Image

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    rows = [dict(row) for row in rows_raw]
    return rows 

title_col1, title_col2, title_col3 = st.columns([1, 5, 1])

image = Image.open('./images/baseball.jpg')
title_col2.header('Baseball Analytics Project', divider='red')
image_col1, image_col2, image_col3 = st.columns([1, 3, 1])
image_col2.image(image)

st.text("")
st.text("")
st.header('Using this app', divider='red')
app_use_text = '''
The purpose of this app is to provide some basic insights into common baseball analytics metrics.  
Valuable information used by baseball front offices is provided for both pitchers and batters.  
Additionally, there are some elements of the app which will pertain to fantasy baseball users 
allowing them to garner useful insights as they prepare for the upcoming season.  All data has 
been retrieved from MLB StatsAPI, Fangraphs, and Baseball Savant.  Any questions or comments 
can be directed to charles.t.clark89@gmail.com.
'''
st.markdown(app_use_text)
st.text("")
st.header('Problem Statement', divider='red')
problem_text = '''
One of the common issues with baseball publications is a disconnect between what they report 
from a statistical perspective and what is utilized by front offices.  While some baseline metrics 
can be useful when evaluating a player, identifying trends is critical for recognizing future value 
for players.  Having worked in a MLB Front Office, I wanted to replicate some of the commonly used 
metrics we utilized to make analytically driven decisions for roster construction.
'''
st.markdown(problem_text)
st.text("")
st.header('Tech Stack', divider='red')
tech_text = '''
This application uses the following technologies to construct robust baseball data pipelines:

* Mage (Orchestration)
* Dbt Cloud (Transformations)
* Google Cloud Storage (Data Lake)
* Google Bigquery (Data Warehouse)
* Terraform (Infrastructure as Code)
* Github (Source Control)
* Github Actions (CI/CD)
* Digital Ocean (Mage Deployment)
* Streamlit (Data Visualization)

All source code is contained in the following repository: https://github.com/ctcb57/baseball-terraform
'''
st.markdown(tech_text)
st.text("")
st.header('Future Work', divider='red')
future_text = '''
The ultimate goal of this project is to build a tool that myself and other can utilize throughout the 
MLB season to assist with player evaluation and fantasy baseball.  While the initial work has focused on 
establishing data pipelines, I believe there is great opportunity to construct Machine Learning models to 
assist with predictive analytics.  The majority of the data contained within this application focuses on 
the Major League level.  However, StatsAPI and Fangraphs provide minor league data as well, so there are 
current plans to incorporate it in the future.
'''
st.markdown(future_text)


# pitch_velo_query = """
# select *
# from (
#   select 
#     s.game_date, 
#     m.pitch_type, 
#     m.avg_pitch_velo
#   from `mlb_dev.fct_pitch_velo_by_game` m 
#   left join `mlb_dev.stg_schedule` s 
#   on m.game_pk = s.game_pk
#   where s.coded_game_state = 'F'
#   and m.pitcher_bam_id = 669302
# )
# pivot 
# (
#   sum(avg_pitch_velo)
#   for pitch_type in ('Slider', 'Splitter', 'Four-seam FB', 'Knuckle Curve', 'Sinker')
# )
# order by game_date asc 
# """
# rows = run_query(pitch_velo_query)

# pitch_velo_df = pd.DataFrame(rows)
# st.line_chart(pitch_velo_df, x="game_date", y=["Slider", "Splitter", "Four-seam FB", "Knuckle Curve", "Sinker"])

