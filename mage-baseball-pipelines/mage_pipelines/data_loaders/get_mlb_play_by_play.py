import requests
from datetime import timedelta
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    # Get Games
    previous_date = str((kwargs.get('execution_date') - timedelta(days=1)).date())
    games_url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={previous_date}"
    games_json = requests.get(games_url).json()
    game_json_list = []
    for schedule_date in games_json['dates']:
        game_pk_list = [x['gamePk'] for x in schedule_date['games'] if x.get('status', {}).get('codedGameState', None) == 'F']
        for game_pk in game_pk_list:
            game_url = f"https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live"
            game_json = requests.get(game_url).json()
            game_json_list.append(game_json)
    return game_json_list 