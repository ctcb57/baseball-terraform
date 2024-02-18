import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    url = "https://statsapi.mlb.com/api/v1/pitchCodes"
    pitch_code_json = requests.get(url).json()
    pitches = []
    for pitch in pitch_code_json:
        data = {
            'pitch_code': pitch.get('code', None), 
            'pitch_code_description': pitch.get('description', None), 
            'swing_status': pitch.get('swingStatus', None), 
            'swing_miss_status': pitch.get('swingMissStatus', None), 
            'swing_contact_status': pitch.get('swingContactStatus', None), 
            'sort_order': pitch.get('sortOrder', None), 
            'strike_status': pitch.get('strikeStatus', None), 
            'ball_status': pitch.get('ballStatus', None), 
            'pitch_status': pitch.get('pitchStatus', None), 
            'pitch_result_text': pitch.get('pitchResultText', None), 
            'created_date': kwargs.get('execution_date')
        }
        pitches.append(data)
    df = pd.DataFrame(pitches)
    return df
