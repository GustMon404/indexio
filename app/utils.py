import json


def remove_value_none_from_dict(value: dict):
    return {key: value for key, value in value.items() if value is not None}


def get_json_if_valid(json_value: str):
    try:
        return json.loads(json_value)
    except json.decoder.JSONDecodeError:
        return None
