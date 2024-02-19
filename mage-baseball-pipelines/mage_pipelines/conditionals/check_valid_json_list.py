if 'condition' not in globals():
    from mage_ai.data_preparation.decorators import condition


@condition
def evaluate_condition(json_list, *args, **kwargs) -> bool:
    if len(json_list) > 0:
        return True
    else: 
        return False
