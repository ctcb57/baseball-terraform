import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    base_url = f"https://statsapi.mlb.com/api/v1/sports"
    sport_data = requests.get(base_url).json()
    df = pd.DataFrame(sport_data['sports'])
    return df


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
