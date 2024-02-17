import pandas as pd
from datetime import datetime, timedelta
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    execution_prev_date = kwargs.get('execution_date') - timedelta(days=1)
    prev_date_year_str = str(execution_prev_date.year)
    prev_date_str = str(execution_prev_date.date())
    mlb_teams_url = f"https://statsapi.mlb.com/api/v1/teams?season={prev_date_year_str}&sportId=1"
    teams_json = requests.get(mlb_teams_url).json()
    team_ids = [x['id'] for x in teams_json['teams']]
    players = []
    for team_id in team_ids:
        team_roster_url = f'https://statsapi.mlb.com/api/v1/teams/{team_id}/roster?date={prev_date_str}'
        team_roster_json = requests.get(team_roster_url).json()
        for player in team_roster_json['roster']:
            player_data = {
                'mlb_bam_id': player.get('person', {}).get('id', None), 
                'full_name': player.get('person', {}).get('fullName', None), 
                'link': player.get('person', {}).get('link', None), 
                'jersey_number': player.get('jerseyNumber', None), 
                'position_code': player.get('position', {}).get('code', None), 
                'position_name': player.get('position', {}).get('name', None), 
                'position_type': player.get('position', {}).get('type', None), 
                'position_abbreviation': player.get('position', {}).get('abbreviation', None), 
                'status_code': player.get('status', {}).get('code', None), 
                'status_description': player.get('status', {}).get('description', None), 
                'parent_team_id': player.get('parentTeamId', None), 
                'current_team_id': team_id, 
                'roster_date': execution_prev_date,
                'created_date': kwargs.get('execution_date')
            }
            players.append(player_data)
    df = pd.DataFrame(players)
    return df
            
