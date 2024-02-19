from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from os import path
from json import loads, dumps
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_big_query(*args, **kwargs):
    """
    Template for loading data from a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    query = '''
    with players_in_game as (
        select *
        from mlb_dev.dim_players_in_game
    ), 
    inactive_players as (
        select *
        from mlb_dev.stg_person
        where is_active = false
        qualify row_number() over (partition by mlb_bam_id order by update_date desc) = 1
    )
    select *
    from players_in_game p
    left join inactive_players i 
    on p.bam_id = i.mlb_bam_id and p.last_game_appearance > extract(date from i.update_date)
    where i.mlb_bam_id is not null 
    and  bam_id not in (
        select distinct mlb_bam_id 
        from mlb_dev.dim_players
    )
    '''
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    df = BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).load(query)
    df_json = df.to_json(orient="records")
    df_json_parsed = loads(df_json)
    return df_json_parsed
