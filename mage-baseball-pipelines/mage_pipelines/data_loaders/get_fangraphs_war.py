import pandas as pd 
from datetime import timedelta
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    execution_prev_date = kwargs.get('execution_date') - timedelta(days=1)
    prev_date_str = str(execution_prev_date.date())
    prev_date_year = str(execution_prev_date.year)
    # Remove when done testing
    prev_date_str = "2023-07-01"
    prev_date_year = "2023"
    url = f"https://www.fangraphs.com/api/leaders/war?season={prev_date_year}&wartype=0&date={prev_date_str}"
    response_json = requests.get(url).json()
    war_data = []
    for item in response_json:
        data = {
            "fg_player_id": item.get("playerid", None), 
            "player_name": item.get("playerName", None), 
            "player_name_route": item.get("playerNameRoute", None), 
            "team_abbreviation": item.get("abbName", None), 
            "team_short_name": item.get("shortName", None), 
            "fg_team_id": item.get("teamId", None), 
            "position": item.get("pos", None), 
            "plate_appearances": item.get("PA", 0.0) if item.get("PA", 0.0) != None else 0.0, 
            "innings_pitched": item.get("IP", 0.0) if item.get("IP", 0.0) != None else 0.0, 
            "pitching_war": item.get("pitWAR", 0.0) if item.get("pitWAR", 0.0) != None else 0.0, 
            "batting_war": item.get("batWAR", 0.0) if item.get("batWAR", 0.0) != None else 0.0, 
            "total_war": item.get("totalWAR", 0.0) if item.get("totalWAR", 0.0) != None else 0.0, 
            "war_date": prev_date_str, 
            "update_date": kwargs.get('execution_date')
        }
        war_data.append(data)

    df = pd.DataFrame(war_data)
    return df
