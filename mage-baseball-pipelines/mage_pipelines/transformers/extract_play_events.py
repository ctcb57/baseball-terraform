import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(json_list, *args, **kwargs):
    play_events = []
    for game in json_list:
        print(f"Processing game data for {game.get('gamePk', None)}")
        for play in game.get('liveData', {}).get('plays', {}).get('allPlays', []):
            # TO DO: iterate to find matchup.batterHotColdZones and matchup.pitcherHotColdZones
            for event in play.get('playEvents', []):
                data = {
                    'game_pk': game.get('gamePk', None), 
                    'play_id': event.get('playId', None), 
                    'at_bat_index': play.get('about', {}).get('atBatIndex', None), 
                    'is_top_inning': play.get('about', {}).get('isTopInning', None), 
                    'inning': play.get('about', {}).get('inning', None),
                    'pitcher_bam_id': play.get('matchup', {}).get('pitcher', {}).get('id', None), 
                    'batter_bam_id': play.get('matchup', {}).get('batter', {}).get('id', None),
                    'play_index': event.get('index', None), 
                    'pitch_number': event.get('pitchNumber', None), 
                    'start_time': event.get('startTime', None), 
                    'endTime': event.get('endTime', None), 
                    'is_pitch': event.get('isPitch', None), 
                    'play_event_type': event.get('type', None), 
                    'play_event_details_call_code': event.get('details', {}).get('call', {}).get('code', None), 
                    'play_event_details_call_desc': event.get('details', {}).get('call', {}).get('description', None), 
                    'play_event_details_desc': event.get('details', {}).get('description', None), 
                    'play_event_details_code': event.get('details', {}).get('code', None), 
                    'is_in_play': event.get('details', {}).get('isInPlay', None), 
                    'is_strike': event.get('details', {}).get('isStrike', None), 
                    'is_ball': event.get('details', {}).get('isBall', None), 
                    'pitch_type_code': event.get('details', {}).get('type', {}).get('code', None), 
                    'pitch_type_desc': event.get('details', {}).get('type', {}).get('description', None), 
                    'is_out': event.get('details', {}).get('isOut', None), 
                    'has_review': event.get('details', {}).get('hasReview', None), 
                    'balls': event.get('count', {}).get('balls', None), 
                    'strikes': event.get('count', {}).get('strikes', None), 
                    'outs': event.get('count', {}).get('outs', None), 
                    'pitch_start_speed': event.get('pitchData', {}).get('startSpeed', None), 
                    'pitch_end_speed': event.get('pitchData', {}).get('endSpeed', None), 
                    'strike_zone_top': event.get('pitchData', {}).get('strikeZoneTop', None), 
                    'strike_zone_bottom': event.get('pitchData', {}).get('strikeZoneBottom', None), 
                    'aY': event.get('pitchData', {}).get('coordinates', {}).get('aY', None), 
                    'aZ': event.get('pitchData', {}).get('coordinates', {}).get('aZ', None), 
                    'pfxX': event.get('pitchData', {}).get('coordinates', {}).get('pfxX', None), 
                    'pX': event.get('pitchData', {}).get('coordinates', {}).get('pX', None), 
                    'pZ': event.get('pitchData', {}).get('coordinates', {}).get('pZ', None), 
                    'vX0': event.get('pitchData', {}).get('coordinates', {}).get('vX0', None), 
                    'vZ0': event.get('pitchData', {}).get('coordinates', {}).get('vZ0', None), 
                    'x': event.get('pitchData', {}).get('coordinates', {}).get('x', None), 
                    'y': event.get('pitchData', {}).get('coordinates', {}).get('y', None), 
                    'x0': event.get('pitchData', {}).get('coordinates', {}).get('x0', None), 
                    'y0': event.get('pitchData', {}).get('coordinates', {}).get('y0', None), 
                    'z0': event.get('pitchData', {}).get('coordinates', {}).get('z0', None), 
                    'aX': event.get('pitchData', {}).get('coordinates', {}).get('aX', None), 
                    'break_angle': event.get('pitchData', {}).get('breaks', {}).get('breakAngle', None), 
                    'break_length': event.get('pitchData', {}).get('breaks', {}).get('breakLength', None), 
                    'break_y': event.get('pitchData', {}).get('breaks', {}).get('breakY', None), 
                    'break_vertical': event.get('pitchData', {}).get('breaks', {}).get('breakVertical', None), 
                    'break_vertical_induced': event.get('pitchData', {}).get('breaks', {}).get('breakVerticalInduced', None), 
                    'break_horizontal': event.get('pitchData', {}).get('breaks', {}).get('breakHorizontal', None), 
                    'spin_rate': event.get('pitchData', {}).get('breaks', {}).get('spinRate', None), 
                    'spin_direction': event.get('pitchData', {}).get('breaks', {}).get('spinDirection', None), 
                    'pitch_zone': event.get('pitchData', {}).get('zone', None), 
                    'pitch_type_confidence': event.get('pitchData', {}).get('typeConfidence', None),
                    'pitch_to_plate_time': event.get('pitchData', {}).get('plateTime', None),
                    'pitcher_extension': event.get('pitchData', {}).get('extension', None),
                    'hit_launch_speed': event.get('hitData', {}).get('launchSpeed', None), 
                    'hit_launch_angle': event.get('hitData', {}).get('launchAngle', None), 
                    'hit_total_distance': event.get('hitData', {}).get('totalDistance', None), 
                    'hit_trajectory': event.get('hitData', {}).get('trajectory', None), 
                    'hit_hardness': event.get('hitData', {}).get('hardness', None), 
                    'hit_location': event.get('hitData', {}).get('location', None), 
                    'hit_coord_x': event.get('hitData', {}).get('coordinates', {}).get('coordX', None), 
                    'hit_coord_y': event.get('hitData', {}).get('coordinates', {}).get('coordY', None), 
                    'created_date': kwargs.get('execution_date')
                }
                play_events.append(data)
    df = pd.DataFrame(play_events)
    return df
