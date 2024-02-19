if 'condition' not in globals():
    from mage_ai.data_preparation.decorators import condition


@condition
def evaluate_condition(data, *args, **kwargs) -> bool:
    if len(data) > 0:
        return True
    else:
        False
            
