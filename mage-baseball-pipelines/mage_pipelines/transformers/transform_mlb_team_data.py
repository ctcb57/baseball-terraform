import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    team_dtypes = {
        'id': pd.Int64Dtype(),
        'season': pd.Int64Dtype(), 
        'parent_org_id': pd.Int64Dtype(), 
        'venue_id': pd.Int64Dtype(), 
        'league_id': pd.Int64Dtype(), 
        'sport_id': pd.Int64Dtype()
    }
    data = data.astype(team_dtypes)
    return data 
    

# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
