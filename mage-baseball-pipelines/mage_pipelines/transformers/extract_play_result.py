import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(json_list, *args, **kwargs):
    plays = []
    for game in json_list:
        print(f"Processing game data for {game.get('gamePk', None)}")
        for play in game.get('liveData', {}).get('plays', {}).get('allPlays', []):
            # TO DO: iterate to find matchup.batterHotColdZones and matchup.pitcherHotColdZones
            data = {
                'game_pk': game.get('gamePk', None), 
                'play_start_time': play.get('about', {}).get('startTime', None), 
                'play_end_time': play.get('about', {}).get('endTime', None), 
                'at_bat_index': play.get('about', {}).get('atBatIndex', None), 
                'is_top_of_inning': True if play.get('about', {}).get('isTopInning', None) == True else False, 
                'inning': play.get('about', {}).get('inning', None), 
                'is_complete': play.get('about', {}).get('isComplete', None), 
                'is_scoring_play': play.get('about', {}).get('isScoringPlay', None), 
                'has_review': play.get('about', {}).get('hasReview', None), 
                'has_out': play.get('about', {}).get('hasOut', None), 
                'captivating_index': play.get('about', {}).get('captivatingIndex', None), 
                'play_type': play.get('result', {}).get('type', None), 
                'play_event': play.get('result', {}).get('event', None), 
                'play_event_type': play.get('result', {}).get('eventType', None), 
                'play_description': play.get('result', {}).get('description', None), 
                'runs_batted_in': play.get('result', {}).get('rbi', None), 
                'away_score': play.get('result', {}).get('awayScore', None), 
                'home_score': play.get('result', {}).get('homeScore', None), 
                'is_out': play.get('result', {}).get('isOut', None), 
                'balls': play.get('count', {}).get('balls', None), 
                'strikes': play.get('count', {}).get('strikes', None), 
                'outs': play.get('count', {}).get('outs', None),
                'batter_bam_id': play.get('matchup', {}).get('batter', {}).get('id', None), 
                'batter_full_name': play.get('matchup', {}).get('batter', {}).get('fullName', None), 
                'batter_link': play.get('matchup', {}).get('batter', {}).get('link', None), 
                'batter_bat_side_code': play.get('matchup', {}).get('batSide', {}).get('code', None), 
                'batter_bat_side_desc': play.get('matchup', {}).get('batSide', {}).get('description', None), 
                'pitcher_bam_id': play.get('matchup', {}).get('pitcher', {}).get('id', None), 
                'pitcher_full_name': play.get('matchup', {}).get('pitcher', {}).get('fullName', None), 
                'pitcher_link': play.get('matchup', {}).get('pitcher', {}).get('link', None), 
                'pitcher_handedness_code': play.get('matchup', {}).get('pitchHand', {}).get('code', None), 
                'pitcher_handedness_desc': play.get('matchup', {}).get('pitchHand', {}).get('description', None), 
                'number_of_play_events': len(play.get('playEvents', []))
            }
            plays.append(data)
    
    df = pd.DataFrame(plays)
    return df 
