import pandas as pd 
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    url = "https://statsapi.mlb.com/api/v1/positions"
    positions_json = requests.get(url).json()
    positions = []
    for position in positions_json:
        data = {
            'position_short_name': position.get('shortName', None), 
            'position_full_name': position.get('fullName', None), 
            'position_abbreviation': position.get('abbrev', None), 
            'position_code': position.get('code', None), 
            'position_type': position.get('type', None), 
            'formal_name': position.get('formalName', None), 
            'display_name': position.get('displayName', None), 
            'is_outfield': position.get('outfield', None), 
            'is_game_position': position.get('gamePosition', None), 
            'is_pitcher': position.get('pitcher', None), 
            'is_fielder': position.get('fielder', None), 
            'created_date': kwargs.get('execution_date')
        }
        positions.append(data)
    df = pd.DataFrame(positions)
    return df
