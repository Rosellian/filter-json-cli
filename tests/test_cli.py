import json
from cli import run

def test_missing_file(tmp_path):
    missing = tmp_path / "does_not_exist.json"

    result = run(["--file", str(missing)])

    assert result.exit_code != 0
    assert "not found" in result.output.lower()

def test_invalid_json(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{invalid json")

    result = run(["--file", str(p)])

    assert result.exit_code != 0
    assert "invalid json" in result.output.lower()

def test_parses_arguments_correctly(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("[]")

    result = run([
        "--file", str(p),
        "--key", "age",
        "--min", "30",
        "--max", "50"
    ])

    assert result.exit_code == 0
    assert result.args.key == ["age"]
    assert result.args.min == 30
    assert result.args.max == 50

def test_filters_data_and_prints_table(tmp_path):
    p = tmp_path / "data.json"
    p.write_text(json.dumps([
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 20}
    ]))

    result = run([
        "--file", str(p),
        "--key", "age",
        "--min", "25"
    ])

    assert "Anna" in result.output
    assert "Bob" not in result.output

def test_filters_data_and_prints_table_max(tmp_path):
    p = tmp_path / "data.json"
    p.write_text(json.dumps([
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 20}
    ]))

    result = run([
        "--file", str(p),
        "--key", "age",
        "--max", "25"
    ])

    assert "Anna" not in result.output
    assert "Bob" in result.output

def test_table_output_format(tmp_path):
    p = tmp_path / "data.json"
    p.write_text('[{"name": "Anna", "age": 30}]')

    result = run(["--file", str(p)])

    assert "name" in result.output
    assert "age" in result.output
    assert "Anna" in result.output
    assert "30" in result.output
    assert "|" in result.output

def test_sorting_output(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Bob", "age": 40},
        {"name": "Anna", "age": 30},
        {"name": "Carl", "age": 20}
    ]
    """)

    result = run([
        "--file", str(p),
        "--sort", "age",
        "--border", "none"
    ])

    output = result.output.splitlines()

    assert "Carl" in output[1]
    assert "Anna" in output[2]
    assert "Bob"  in output[3]

def test_sorting_descending(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Bob", "age": 40},
        {"name": "Anna", "age": 30},
        {"name": "Carl", "age": 20}
    ]
    """)

    result = run([
        "--file", str(p),
        "--sort", "age",
        "--desc",
        "--border", "none"
    ])

    output = result.output.splitlines()

    assert "Bob"  in output[1]
    assert "Anna" in output[2]
    assert "Carl" in output[3]

def test_equals_filter(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 30},
        {"name": "Carl", "age": 20}
    ]
    """)

    result = run([
        "--file", str(p),
        "--key", "age",
        "--equals", "30"
    ])

    result.output.splitlines()

    assert "Anna" in result.output
    assert "Bob" in result.output
    assert "Carl" not in result.output

def test_contains_filter(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna"},
        {"name": "Annalise"},
        {"name": "Bob"}
    ]
    """)

    result = run([
        "--file", str(p),
        "--key", "name",
        "--contains", "anna"
    ])

    assert "Anna" in result.output
    assert "Annalise" in result.output
    assert "Bob" not in result.output

def test_multiple_keys_and_filters(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna", "age": 30},
        {"name": "Annalise", "age": 20},
        {"name": "Bob", "age": 40}
    ]
    """)

    result = run([
        "--file", str(p),
        "--key", "name",
        "--contains", "anna",
        "--key", "age",
        "--min", "25"
    ])

    assert "Anna" in result.output
    assert "Annalise" not in result.output
    assert "Bob" not in result.output

def test_json_output(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 20}
    ]
    """)

    result = run([
        "--file", str(p),
        "--json"
    ])

    parsed = json.loads(result.output)

    assert isinstance(parsed, list)
    assert parsed[0]["name"] == "Anna"
    assert parsed[1]["name"] == "Bob"

def test_regex_filter(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna"},
        {"name": "Annalise"},
        {"name": "Bob"},
        {"name": "ANNA-MARIA"}
    ]
    """)

    result = run([
        "--file", str(p),
        "--key", "name",
        "--regex", "^anna"
    ])

    assert "Anna" in result.output
    assert "Annalise" in result.output
    assert "ANNA-MARIA" in result.output
    assert "Bob" not in result.output

def test_no_color_output(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna", "age": 30}
    ]
    """)

    result = run([
        "--file", str(p),
        "--no-color"
    ])

    assert "\033[" not in result.output

def test_not_contains_filter(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna"},
        {"name": "Bob"},
        {"name": "Annalise"},
        {"name": "Carl"}
    ]
    """)

    result = run([
        "--file", str(p),
        "--key", "name",
        "--not-contains", "anna"
    ])

    assert "Bob" in result.output
    assert "Carl" in result.output
    assert "Anna" not in result.output
    assert "Annalise" not in result.output

def test_invert_filter(tmp_path):
    p = tmp_path / "data.json"
    p.write_text("""
    [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 20},
        {"name": "Carl", "age": 40}
    ]
    """)

    result = run([
        "--file", str(p),
        "--key", "age",
        "--min", "30",
        "--invert",
        "--no-color",
        "--json"
    ])

    assert "Bob" in result.output
    assert "Anna" not in result.output
    assert "Carl" not in result.output

def test_max_width_flag(tmp_path):
    p = tmp_path / "data.json"
    p.write_text('[{"text": "abcdefghijklmnopqrstuvwxyz"}]')

    result = run([
        "--file", str(p),
        "--max-width", "10"
    ])

    assert "abcdefghi…" in result.output