import pandas as pd
from datetime import timedelta
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    execution_prev_date = kwargs.get('execution_date') - timedelta(days=1)
    prev_date_str = str(execution_prev_date.date())
    url = f"https://statsapi.mlb.com/api/v1/people/changes?updatedSince={prev_date_str}"   
    person_json = requests.get(url).json()
    players = []
    for person in person_json['people']:
        person_data = {
            "mlb_bam_id": person.get('id', None), 
            "full_name": person.get('fullName', None), 
            "link": person.get('link', None), 
            "first_name": person.get('firstName', None), 
            "last_name": person.get('lastName', None), 
            "primary_number": person.get('primaryNumber', None), 
            "birth_date": person.get('birthDate', None), 
            "current_age": person.get('currentAge', None), 
            "birth_city": person.get('birthCity', None), 
            "birth_state_province": person.get('birthStateProvince', None), 
            "birth_country": person.get('birthCountry', None), 
            "height": person.get('height', None), 
            "weight": person.get('weight', None), 
            "active": person.get('active', None), 
            "primary_position_code": person.get('primaryPosition', {}).get('code', None), 
            "primary_position_name": person.get('primaryPosition', {}).get('name', None), 
            "primary_position_type": person.get('primaryPosition', {}).get('type', None), 
            "primary_position_abbreviation": person.get('primaryPosition', {}).get('abbreviation', None), 
            "used_name": person.get('useName', None), 
            "used_last_name": person.get('useLastName', None), 
            "middle_name": person.get('middleName', None), 
            "boxscoreName": person.get('boxscoreName', None), 
            "nickname": person.get('nickName', None), 
            "gender": person.get('gender', None), 
            "is_player": person.get('isPlayer', None), 
            "is_verified": person.get('isVerified', None), 
            "draft_year": person.get('draftYear', None), 
            "mlb_debut_date": person.get('mlbDebutDate', None), 
            "bat_side_code": person.get('batSide', {}).get('code', None), 
            "bat_side_description": person.get('batSide', {}).get('description', None), 
            "name_first_last": person.get('nameFirstLast', None), 
            "name_slug": person.get('nameSlug', None), 
            "first_last_name": person.get('firstLastName', None), 
            "last_first_name": person.get('lastFirstName', None), 
            "last_init_name": person.get('lastInitName', None), 
            "init_last_name": person.get('initLastName', None), 
            "full_fml_name": person.get('fullFMLName', None), 
            "full_lfm_name": person.get('fullLFMName', None), 
            "strike_zone_top": person.get('strikeZoneTop', None), 
            "strike_zone_bottom": person.get('strikeZoneBottom', None), 
            "update_date": execution_prev_date, 
            "created_date": kwargs.get('execution_date')
        }
        players.append(person_data)
    
    df = pd.DataFrame(players)
    return df 
