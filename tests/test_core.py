from core import filter_data

def test_no_filter_returns_all():
    data = [{"name": "Anna", "age": 30}, {"name": "Bob", "age": 40}]
    assert filter_data(data, {}) == data

def test_filter_exact_match():
    data = [{"name": "Anna"}, {"name": "Bob"}]
    assert filter_data(data, {"name": "Anna"}) == [{"name": "Anna"}]

def test_filter_min_value():
    data = [{"age": 20}, {"age": 40}]
    assert filter_data(data, {"min_age": 30}) == [{"age": 40}]

def test_filter_max_value():
    data = [{"age": 20}, {"age": 40}]
    assert filter_data(data, {"max_age": 30}) == [{"age": 20}]

def test_combined_filters():
    data = [{"age": 25}, {"age": 35}, {"age": 45}]
    filters = {"min_age": 30, "max_age": 40}
    assert filter_data(data, filters) == [{"age": 35}]

