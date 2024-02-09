import pandas as pd 
import requests 
from datetime import datetime, timedelta

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    year_str = str(kwargs.get('execution_date').year)
    # year_str = '2023'
    print(f"Processing team data for year: {year_str}")
    base_url = f"https://statsapi.mlb.com/api/v1/teams?season={year_str}"
    team_json = requests.get(base_url).json()
    team_list = []
    for team in team_json['teams']:
        team_dict = {
            'id': team.get('id', None),
            'season': team.get('season', None),
            'full_team_name': team.get('name', None),
            'team_name': team.get('teamName', None),
            'location_name': team.get('locationName', None),
            'short_name': team.get('shortName', None),
            'parent_org_name': team.get('parentOrgName', None),
            'parent_org_id': team.get('parentOrgId', None),
            'franchise_name': team.get('franchiseName', None),
            'club_name': team.get('clubName', None),
            'team_code': team.get('teamCode', None),
            'abbreviation': team.get('abbreviation', None),
            'first_year_of_play': team.get('firstYearOfPlay', None),
            'team_mlb_link': team.get('link', None),
            'file_code': team.get('fileCode', None),
            'all_star_status': team.get('allStarStatus', None), 
            'venue_id': team.get('venue', {}).get('id', None),
            'venue_name': team.get('venue', {}).get('name', None),
            'venue_mlb_link': team.get('venue', {}).get('link', None),
            'league_id': team.get('league', {}).get('id', None),
            'league_name': team.get('league', {}).get('name', None),
            'league_mlb_link': team.get('league', {}).get('link', None),
            'division_id': team.get('division', {}).get('id', None),
            'division_name': team.get('division', {}).get('name', None),
            'division_mlb_link': team.get('division', {}).get('link', None),
            'sport_id': team.get('sport', {}).get('id', None),
            'sport_name': team.get('sport', {}).get('name', None),
            'sport_mlb_link': team.get('sport', {}).get('link', None),
            'is_active': team.get('active', None), 
            'updated_date': pd.Timestamp.now()
        }
        team_list.append(team_dict)
    df = pd.DataFrame(team_list)
    return df

    


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined