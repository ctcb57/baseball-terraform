import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd 
import numpy as np
import requests
import time

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

title_col1, title_col2, title_col3 = st.columns([1, 5, 1])
title_col2.header('Pitching', divider='red')
st.write("")
st.write("")

head_shot_url_start = "https://img.mlbstatic.com/mlb-photos/image/upload/w_62,d_people:generic:headshot:silo:current.png,q_auto:best,f_auto/v1/people/"
head_shot_url_end = "/headshot/83/current"

def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    rows = [dict(row) for row in rows_raw]
    return rows 

def get_pitchers():
    pitcher_list_query = '''
    select *
    from `mlb_dev.dim_mlb_pitcher_list`
    order by full_name asc
    '''
    rows = run_query(pitcher_list_query)
    return rows

def get_pitcher_data(option):
    if option:
        st.session_state.selected_pitcher = [x for x in st.session_state.pitcher_list if option == x['full_name']]
        pitcher_data = st.session_state.selected_pitcher[0]
        print(pitcher_data)
        st.session_state.pitcher_headshot_url = f"{head_shot_url_start}{pitcher_data['mlb_bam_id']}{head_shot_url_end}"

        pitch_type_query = '''
        select 
            distinct pitch_type
        from `mlb_dev.fct_pitch_velo_by_game`
        where pitcher_bam_id = {0}
        '''.format(pitcher_data['mlb_bam_id'])
        rows = run_query(pitch_type_query)
        pitch_types = [x['pitch_type'] for x in rows]
        pitch_types_str_quotes = ', '.join([f"'{x['pitch_type']}'" for x in rows])
        pitch_types_str = [f"{x['pitch_type']}" for x in rows]
        print(pitch_types)
        pitch_velo_query = '''
        select * except(game_pk)
        from (
            select
                m.game_date,
                m.game_pk, 
                m.pitch_type, 
                m.avg_pitch_velo
            from `mlb_dev.fct_pitch_velo_by_game` m 
            where m.pitcher_bam_id = {0}
        )
        pivot
        (
            sum(avg_pitch_velo)
            for pitch_type in ({1})
        )
        '''.format(pitcher_data['mlb_bam_id'], pitch_types_str_quotes)
        print(pitch_velo_query)
        velo_rows = run_query(pitch_velo_query)
        st.session_state.pitch_types = pitch_types_str
        print(type(st.session_state.pitch_types))
        pitch_velo_df = pd.DataFrame(velo_rows)
        st.session_state.pitch_velo_df = pitch_velo_df


        

if 'pitcher_id' not in st.session_state:
    st.session_state.pitcher_id = ''

if 'selected_pitcher' not in st.session_state:
    st.session_state.selected_pitcher = []
    st.session_state.displayed_pitcher = []

if 'pitcher_list' not in st.session_state:
    st.session_state.pitcher_list = get_pitchers() 
    pitcher_names = [x['full_name'] for x in st.session_state.pitcher_list]
    st.session_state.pitcher_names = pitcher_names
    st.session_state.selected_pitcher = []

# if 'pitch_velo_df' not in st.session_state:
#     holder = [{'a': 1}]

with st.form("pitcher_search"):
    pitcher_option = st.selectbox(
        "Select a pitcher", 
        st.session_state.pitcher_names, 
        index=None, 
        placeholder="Pitcher...", 
        key=st.session_state.displayed_pitcher
    )
    st.form_submit_button('Submit Name', on_click=get_pitcher_data(pitcher_option))

st.write("")
st.write("")
if 'selected_pitcher' in st.session_state and len(st.session_state['selected_pitcher']):
    player_data = st.session_state['selected_pitcher'][0]
    st.header(f"{player_data['full_name']}", divider='blue')
    bio_col1, bio_col2, bio_col3, bio_col4, bio_col5 = st.columns([1, 1, 1, 1, 1])
    bio_col1.image(st.session_state['pitcher_headshot_url'])
    bio_col2.text(f"Age: {player_data['current_age']}")
    bio_col2.text(f"Height: {player_data['height']}")
    bio_col3.text(f"Team: {player_data['abbreviation']}")
    bio_col3.text(f"Weight: {player_data['weight']}")
    bio_col4.text(f"Position: {player_data['pitch_hand_code']}HP")
    bio_col4.text(f"Drafted: {player_data['draft_year'] if player_data['draft_year'] else 'N/A'}")
    bio_col5.text(f"Jersey: {player_data['jersey_number']}")
    bio_col5.text(f"Deb: {player_data['mlb_debut_date'].strftime('%m/%d/%Y')}")
    st.write("")
    st.write("")
    st.session_state['selected_pitcher'] = []

    if 'pitch_velo_df' in st.session_state:
        tab1, tab2 = st.tabs(["Pitch Velo by Month", "Other Metric"])
        tab1.line_chart(st.session_state.pitch_velo_df, x="game_date", y=st.session_state.pitch_types)

    
    # tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    # data = np.random.randn(10, 1)

    # tab1.subheader("A tab with a chart")
    # tab1.line_chart(data)

    # tab2.subheader("A tab with the data")
    # tab2.write(data)

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