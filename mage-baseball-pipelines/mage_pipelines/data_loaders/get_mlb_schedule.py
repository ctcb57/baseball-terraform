import pandas as pd
import requests 
from datetime import datetime, timedelta 

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    previous_date = str((kwargs.get('execution_date') - timedelta(days=1)).date())
    # Remove this when ready to merge
    previous_date = '2023-05-01'
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={previous_date}"
    schedule_json = requests.get(url).json()
    games_data_list = []
    if len(schedule_json['dates']):
        for schedule_date in schedule_json['dates']:
            games_list = [x for x in schedule_date['games']]
            for game in games_list:
                game_dict = {
                    'game_pk': game.get('gamePk', None), 
                    'game_guid': game.get('gameGuid', None), 
                    'link': game.get('link', None), 
                    'game_type': game.get('gameType', None), 
                    'season': game.get('season', None), 
                    'game_date': game.get('gameDate', None), 
                    'official_date': game.get('officialDate', None), 
                    'abstract_game_state': game.get('status', {}).get('abstractGameState', None), 
                    'coded_game_state': game.get('status', {}).get('codedGameState', None), 
                    'detailed_state': game.get('status', {}).get('detailedState', None), 
                    'status_code': game.get('status', {}).get('statusCode', None), 
                    'is_start_time_tbd': game.get('status', {}).get('startTimeTBD', None), 
                    'abstract_game_code': game.get('status', {}).get('abstractGameCode', None), 
                    'away_team_wins': game.get('teams', {}).get('away', {}).get('leagueRecord', {}).get('wins', None), 
                    'away_team_losses': game.get('teams', {}).get('away', {}).get('leagueRecord', {}).get('losses', None), 
                    'away_team_win_pct': game.get('teams', {}).get('away', {}).get('leagueRecord', {}).get('pct', None), 
                    'away_team_score': game.get('teams', {}).get('away', {}).get('score', None), 
                    'away_team_id': game.get('teams', {}).get('away', {}).get('team', {}).get('id', None), 
                    'away_team_name': game.get('teams', {}).get('away', {}).get('team', {}).get('name', None), 
                    'away_team_is_winner': game.get('teams', {}).get('away', {}).get('isWinner', None), 
                    'away_team_is_split_squad': game.get('teams', {}).get('away', {}).get('splitSquad', None), 
                    'away_team_series_number': game.get('teams', {}).get('away', {}).get('seriesNumber', None),
                    'home_team_wins': game.get('teams', {}).get('home', {}).get('leagueRecord', {}).get('wins', None), 
                    'home_team_losses': game.get('teams', {}).get('home', {}).get('leagueRecord', {}).get('losses', None), 
                    'home_team_win_pct': game.get('teams', {}).get('home', {}).get('leagueRecord', {}).get('pct', None), 
                    'home_team_score': game.get('teams', {}).get('home', {}).get('score', None), 
                    'home_team_id': game.get('teams', {}).get('home', {}).get('team', {}).get('id', None), 
                    'home_team_name': game.get('teams', {}).get('home', {}).get('team', {}).get('name', None), 
                    'home_team_is_winner': game.get('teams', {}).get('home', {}).get('isWinner', None), 
                    'home_team_is_split_squad': game.get('teams', {}).get('home', {}).get('splitSquad', None), 
                    'home_team_series_number': game.get('teams', {}).get('home', {}).get('seriesNumber', None),
                    'venue_id': game.get('venue', {}).get('id', None), 
                    'venue_name': game.get('venue', {}).get('name', None), 
                    'content_link': game.get('content', {}).get('link', None), 
                    'is_tie': game.get('isTie', None), 
                    'game_number': game.get('gameNumber', None), 
                    'double_header': game.get('doubleHeader', None), 
                    'gameday_type': game.get('gamedayType', None), 
                    'tiebreaker': game.get('tiebreaker', None), 
                    'is_day_game': True if game.get('dayNight', None) == 'day' else False, 
                    'scheduled_innings': game.get('scheduledInnings', None), 
                    'created_date': datetime.now()
                }
                games_data_list.append(game_dict)
    df = pd.DataFrame(games_data_list)
    return df
