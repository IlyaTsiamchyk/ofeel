import copy

VALUE_WEIGHTS = {
    'proteinsNumber': 1.2
}


def create_diet(dishes, food_types):
    diet = {}

    BODY_REQUIREMENTS = get_body_requirements()
    left_body_requirements = copy.copy(BODY_REQUIREMENTS)

    count_use_value(dishes[0], left_body_requirements, BODY_REQUIREMENTS)

    return diet


def count_use_value(dish, requirements_left, total_requirements):
    temp_value_weights = get_temp_weights(requirements_left, total_requirements)

    test = dish.proteinsNumber * temp_value_weights['proteinsNumber']
    requirements_left['proteinsNumber'] = requirements_left['proteinsNumber'] - 10
    test2 = requirements_left['proteinsNumber']
    pass

def get_body_requirements():
    BODY_REQUIREMENTS = {
        'proteinsNumber': 100
    }
    #TODO: add personal height etc counting

    return BODY_REQUIREMENTS


def get_temp_weights(requirements_left, total_requirements):
    temp_value_weights = copy.copy(VALUE_WEIGHTS)

    for key in temp_value_weights:
        temp_value_weights[key] = temp_value_weights[key] + requirements_left[key] / total_requirements[key]

    return temp_value_weights