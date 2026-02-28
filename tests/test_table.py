from table import format_table, NO_BORDER, set_color_enabled


def test_format_table_basic():
    items = [{"name": "Anna", "age": 30}]
    output = format_table(items)

    assert "name" in output
    assert "age" in output
    assert "Anna" in output
    assert "30" in output
    assert "|" in output

def test_format_table_alignment():
    items = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 20}
    ]
    set_color_enabled(False)
    output = format_table(items, border="none")
    lines = output.splitlines()

    assert len(lines[0].split("|")) == len(lines[1].split("|"))

def test_table_handles_missing_fields():
    items = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "city": "Gothenburg"}
    ]

    set_color_enabled(False)
    output = format_table(items, border="none")
    lines = output.splitlines()

    assert "age" in lines[0]
    assert "city" in lines[0]
    assert "name" in lines[0]

    assert "Anna" in lines[1]
    assert "Gothenburg" not in lines[1]

    assert "Bob" in lines[2]
    assert "30" not in lines[2]

def test_numeric_alignment():
    items = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 8}
    ]

    set_color_enabled(False)
    output = format_table(items, border="none")
    lines = output.splitlines()

    header, row1, row2 = lines

    age_index = header.index("age")

    print(f"\n{output}")

    assert row1.index("30") == age_index + 1
    assert row2.index("8") == age_index + 2

def test_table_truncates_long_values():
    items = [
        {"name": "Anna", "description": "This is a very long description that should be truncated"}
    ]

    output = format_table(items, max_width=20)

    assert "This is a very long…" in output