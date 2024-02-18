import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    url = "https://statsapi.mlb.com/api/v1/eventTypes"
    event_type_json = requests.get(url).json()
    event_types = []
    for event in event_type_json:
        data = {
            'event_type_code': event.get('code', None), 
            'event_type_description': event.get('description', None), 
            'is_plate_appearance': event.get('plateAppearance', None), 
            'is_hit': event.get('hit', None), 
            'is_base_running_event': event.get('baseRunningEvent', None), 
            'created_date': kwargs.get('execution_date')
        }
        event_types.append(data)
    
    df = pd.DataFrame(event_types)
    return df 