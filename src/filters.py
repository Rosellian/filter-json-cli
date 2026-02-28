import re

def filter_contains(field, items, value):
    return [item for item in items if item[field] is not None and value.lower() in str(item[field].lower())]

def filter_not_contains(field, items, value):
    return [item for item in items if item[field] is None or not value.lower() in str(item[field].lower())]

def filter_equals(field, items, value):
    return [item for item in items if str(item.get(field)) == str(value)]

def filter_not_equals(field, items, value):
    return [item for item in items if str(item.get(field)) != str(value)]

def filter_max(field, items, value):
    return [item for item in items if item.get(field) is not None and item.get(field) <= value]

def filter_min(field, items, value):
    return [item for item in items if item.get(field) is not None and item.get(field) >= value]

def filter_regex(field, items, pattern):
    regex = re.compile(pattern, re.IGNORECASE)
    return [
        item for item in items
        if item.get(field) is not None and regex.search(str(item.get(field)))
    ]

def filter_not_regex(field, items, pattern):
    regex = re.compile(pattern, re.IGNORECASE)
    return [
        item for item in items
        if item.get(field) is None or not regex.search(str(item.get(field)))
    ]