import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    war_dtypes = {
        'fg_player_id': pd.Int64Dtype(), 
        'fg_team_id': pd.Int64Dtype(), 
        'plate_appearances': float, 
        'innings_pitched': float,
        'pitching_war': float, 
        'batting_war': float, 
        'total_war': float
    }
    data = data.astype(war_dtypes)
    return data 
