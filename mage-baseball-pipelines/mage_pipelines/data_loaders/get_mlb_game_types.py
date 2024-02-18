import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    url = "https://statsapi.mlb.com/api/v1/gameTypes"
    game_type_json = requests.get(url).json()
    game_types = []
    for game_type in game_type_json:
        data = {
            'game_type_id': game_type.get('id', None), 
            'game_type_description': game_type.get('description', None), 
            'created_date': kwargs.get('execution_date')
        }
        game_types.append(data)
    df = pd.DataFrame(game_types)
    return df 
