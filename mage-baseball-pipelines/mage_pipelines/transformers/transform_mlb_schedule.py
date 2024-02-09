import pandas as pd 

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    schedule_dtypes = {
        'game_pk': pd.Int64Dtype(), 
        'away_team_wins': pd.Int64Dtype(), 
        'away_team_losses': pd.Int64Dtype(), 
        'away_team_score': pd.Int64Dtype(), 
        'away_team_id': pd.Int64Dtype(),
        'away_team_series_number': pd.Int64Dtype(), 
        'home_team_wins': pd.Int64Dtype(), 
        'home_team_losses': pd.Int64Dtype(), 
        'home_team_score': pd.Int64Dtype(), 
        'home_team_id': pd.Int64Dtype(),
        'home_team_series_number': pd.Int64Dtype(), 
        'venue_id': pd.Int64Dtype(), 
        'game_number': pd.Int64Dtype(), 
        'scheduled_innings': pd.Int64Dtype()
    }
    data = data.astype(schedule_dtypes)
    return data

