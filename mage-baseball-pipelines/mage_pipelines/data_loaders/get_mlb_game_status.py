import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    url = "https://statsapi.mlb.com/api/v1/gameStatus"
    game_json = requests.get(url).json()
    games = []
    for game in game_json:
        data = {
            'abstract_game_state': game.get('abstractGameState', None), 
            'coded_game_state': game.get('codedGameState', None), 
            'detailed_state': game.get('detailedState', None), 
            'status_code': game.get('statusCode', None), 
            'abstract_game_code': game.get('abstractGameCode', None), 
            'created_date': kwargs.get('execution_date')
        }
        games.append(data)
    
    df = pd.DataFrame(games)
    return df
