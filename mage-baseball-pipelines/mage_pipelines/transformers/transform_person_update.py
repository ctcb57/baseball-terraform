import pandas as pd 

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    person_dtypes = {
        'mlb_bam_id': pd.Int64Dtype(), 
        'active': bool, 
        'is_player': bool, 
        'is_verified': bool, 
        'strike_zone_top': float, 
        'strike_zone_bottom': float
    }
    data = data.astype(person_dtypes)
    return data

