import pandas as pd 
import requests 
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    now_str = str(kwargs.get('execution_date').year)
    base_url = f"https://statsapi.mlb.com/api/v1/teams?season={now_str}"
    team_json = requests.get(base_url).json()
    team_list = []
    for team in team_json['teams']:
        team_dict = {
            'id': team['id'],
            'season': team['season'],
            'full_team_name': team['name'],
            'team_name': team['teamName'],
            'location_name': team['locationName'],
            'short_name': team['shortName'],
            'parent_org_name': team['parentOrgName'],
            'parent_org_id': team['parentOrgId'],
            'franchise_name': team['franchiseName'],
            'club_name': team['clubName'],
            'team_code': team['teamCode'],
            'abbreviation': team['abbreviation'],
            'first_year_of_play': team['firstYearOfPlay'],
            'team_mlb_link': team['link'],
            'file_code': team['fileCode'],
            'all_star_status': team['allStarStatus'], 
            'venue_id': team.get('venue', {}).get('id', ''),
            'venue_name': team.get('venue', {}).get('name', ''),
            'venue_mlb_link': team.get('venue', {}).get('link', ''),
            'league_id': team.get('league', {}).get('id', ''),
            'league_name': team.get('league', {}).get('name', ''),
            'league_mlb_link': team.get('league', {}).get('link', ''),
            'division_id': team.get('division', {}).get('id', ''),
            'division_name': team.get('division', {}).get('name', ''),
            'division_mlb_link': team.get('division', {}).get('link', ''),
            'sport_id': team.get('sport', {}).get('id', ''),
            'sport_name': team.get('sport', {}).get('name', ''),
            'sport_mlb_link': team.get('sport', {}).get('link', ''),
            'is_active': team['active']
        }
        team_list.append(team_dict)
        df = pd.DataFrame(team_list)
        print(df.head())

    


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
