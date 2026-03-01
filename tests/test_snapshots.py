import pathlib

from core import apply_select
from table import format_table, set_color_enabled

SNAPSHOT_DIR = pathlib.Path(__file__).parent / "snapshots"

def load_snapshot(name):
    return (SNAPSHOT_DIR / name).read_text().rstrip("\n")

def assert_snapshot(name, value):
    expected = load_snapshot(name)
    assert value.rstrip("\n") == expected, (
        f"Snapshot mismatch for {name}.\n"
        f"--- expected\n{expected}\n"
        f"--- got\n{value}"
    )

def test_table_ascii_snapshot(monkeypatch):
    set_color_enabled(False)
    items = [
        {"name": "Anna", "age": 30, "city": "Halmstad"},
        {"name": "Bob", "age": 8, "city": "Göteborg"},
    ]

    output = format_table(items, border="ascii")
    assert_snapshot("table_basic.txt", output)

def test_table_unicode_snapshot(monkeypatch):
    set_color_enabled(False)
    items = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 8},
    ]

    output = format_table(items, border="unicode")
    assert_snapshot("table_unicode.txt", output)

def test_table_no_color_snapshot(monkeypatch):
    set_color_enabled(False)
    items = [{"name": "Anna", "age": 30}]

    output = format_table(items, border="ascii")
    assert_snapshot("table_no_color.txt", output)

def test_table_max_width_snapshot(monkeypatch):
    set_color_enabled(False)
    items = [{"text": "abcdefghijklmnopqrstuvwxyz"}]

    output = format_table(items, border="ascii", max_width=10)
    assert_snapshot("table_max_width.txt", output)

def test_select_with_alias_snapshot():
    items = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 8},
    ]

    output = format_table(
        apply_select(items, ["name", "age"], {"name": "n", "age": "a"}),
        border="ascii"
    )

    assert_snapshot("table_select_alias.txt", output)