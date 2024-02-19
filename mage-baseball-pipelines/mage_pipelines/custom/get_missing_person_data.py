import pandas as pd 
import requests
if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(person_list: list, *args, **kwargs):
    base_url = "https://statsapi.mlb.com/api/v1/people"
    player_id_list = [str(x['bam_id']) for x in person_list]
    player_ids_str = ','.join(player_id_list)
    url = f"{base_url}?personIds={player_ids_str}"
    print(f"Loading data for {len(person_list)} players")
    players_json = requests.get(url).json()
    players_to_load = []
    for person in players_json['people']:
        data = {
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
            "pitch_hand_code": person.get('pitchHand', {}).get('code', None), 
            'pitch_hand_description': person.get('pitchHand', {}).get('description', None),
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
            "update_date": kwargs.get('execution_date'), 
            "created_date": kwargs.get('execution_date')
        }
        players_to_load.append(data)
    
    print("Successful retrieved all missing players from API")
    df = pd.DataFrame(players_to_load)
    return df 
