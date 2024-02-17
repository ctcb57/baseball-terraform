import pandas as pd 
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    roster_dtypes = {
        'mlb_bam_id': pd.Int64Dtype(), 
        'full_name': str, 
        'link': str, 
        'jersey_number': str, 
        'position_code': str, 
        'position_name': str, 
        'position_abbreviation': str, 
        'status_code': str, 
        'status_description': str, 
        'parent_team_id': pd.Int64Dtype(), 
        'current_team_id': pd.Int64Dtype()
    }
    data = data.astype(roster_dtypes)
    return data 

