import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    url = "https://statsapi.mlb.com/api/v1/pitchTypes"
    pitch_types_json = requests.get(url).json()
    pitches = []
    for pitch in pitch_types_json:
        data = {
            'pitch_type_code': pitch.get('code', None), 
            'pitch_type_description': pitch.get('description', None),
            'created_date': kwargs.get('execution_date')
        }
        pitches.append(data)
    df = pd.DataFrame(pitches)
    return df
