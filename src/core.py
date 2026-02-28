from filters import (filter_min, filter_max, filter_equals, filter_not_equals, filter_contains,
                                filter_not_contains, filter_regex, filter_not_regex)

NOT_ = "not_"
CONTAINS_ = "contains_"
NOT_CONTAINS_ = NOT_+CONTAINS_

REGEX_ = "regex_"
NOT_REGEX_ = NOT_+REGEX_

EQ_ = "eq_"
NOT_EQ_ = NOT_+EQ_


def filter_data(data: list[dict], data_filter):
    if not data_filter:
        return data

    result = data

    for key, value in data_filter.items():
        if key.startswith("min_"):
            field = key[4:]
            result = filter_min(field, result, value)
        elif key.startswith("max_"):
            field = key[4:]
            result = filter_max(field, result, value)
        elif key.startswith(EQ_):
            field = key[len(EQ_):]
            result = filter_equals(field, result, value)
        elif key.startswith(NOT_EQ_):
            field = key[len(NOT_EQ_):]
            result = filter_not_equals(field, result, value)
        elif key.startswith(CONTAINS_):
            field = key[len(CONTAINS_):]
            result = filter_contains(field, result, value)
        elif key.startswith(NOT_CONTAINS_):
            field = key[len(NOT_CONTAINS_):]
            result = filter_not_contains(field, result, value)
        elif key.startswith(REGEX_):
            field = key[len(REGEX_):]
            result = filter_regex(field, result, value)
        elif key.startswith(NOT_REGEX_):
            field = key[len(NOT_REGEX_):]
            result = filter_not_regex(field, result, value)
        else:
            result = [item for item in result if item.get(key) == value]
    return result

def apply_select(items, fields):
    if not fields:
        return items
    result = []
    for item in items:
        filtered = {k: v for k, v in item.items() if k in fields}
        result.append(filtered)

    return result