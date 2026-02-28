import argparse
import os
import json
import sys

from argparse_ext import build_filters_from_argv
from core import filter_data, apply_select
from helptext import HELP_TEXTS
from table import format_table, set_color_enabled

class Result:
    def __init__(self, exit_code, output, args=None):
        self.exit_code = exit_code
        self.output = output
        self.args = args

def run(argv):
    args = parse_args(argv)

    selected_fields = None
    if args.select:
        selected_fields = [field.strip() for field in args.select.split(",")]

    args._argv = argv

    if not os.path.exists(args.file):
        return Result(1, f"File '{args.file}' not found.", args)

    try:
        with open(args.file) as f:
            data = json.load(f)
    except Exception:
        return Result(1, "Invalid JSON.", args)

    filters = build_filters_from_argv(args)
    filtered = filter_data(data, filters)

    filtered = invert_items(filtered, data, args.invert)
    if selected_fields:
        filtered = apply_select(filtered, selected_fields)
    filtered = sort_items(filtered, args.sort, args.desc)

    if args.json:
        return Result(0, json.dumps(filtered), args)

    set_color_enabled(not args.no_color)
    output = format_table(filtered, max_width=args.max_width, border=args.border)
    return Result(0, output, args)


def invert_items(filtered, data, invert):
    if not invert:
        return filtered

    filtered_set = {id(item): item for item in filtered}
    return [item for item in data if id(item) not in filtered_set]


def sort_items(items, sort_key, descending=False):
    if not sort_key:
        return items
    return sorted(items, key=lambda item: item[sort_key], reverse=descending)

def parse_args(argv):
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--lang", choices=["sv", "en"], default="sv")
    pre_args, _ = pre_parser.parse_known_args(argv)

    parser = argparse.ArgumentParser(description=HELP_TEXTS[pre_args.lang],
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", required=True,
                        help="JSON-fil att läsa in (måste innehålla en lista av objekt).")
    parser.add_argument("--key", action="append",
                        help="Sätter aktivt fält för efterföljande filter. Kan anges flera gånger.")
    parser.add_argument("--min", type=int,
                        help="Matchar poster där fältet är större än eller lika med värdet.")
    parser.add_argument("--max", type=int,
                        help="Matchar poster där fältet är mindre än eller lika med värdet.")
    parser.add_argument("--equals", help="Matchar poster där fältet är exakt lika med värdet.")
    parser.add_argument("--not-equals", help="Matchar poster där fältet INTE är lika med värdet.")
    parser.add_argument("--contains",
                        help="Matchar poster där fältet innehåller texten (case-insensitive).")
    parser.add_argument("--not-contains", help="Matchar poster där fältet INTE innehåller texten.")
    parser.add_argument("--regex",
                        help="Matchar poster där fältet matchar regex-mönstret (case-insensitive).")
    parser.add_argument("--not-regex", help="Matchar poster där fältet INTE matchar regex-mönstret.")
    parser.add_argument("--sort", help="Sorterar resultatet på angivet fält.")
    parser.add_argument("--desc", action="store_true", help="Sorterar i fallande ordning.")
    parser.add_argument("--invert", action="store_true",
                        help="Inverterar hela resultatet efter filtrering.")
    parser.add_argument("--select",
                        help="Comma-separated list of fields to include in the output table.")
    parser.add_argument("--json", action="store_true",
                        help="Skriver ut resultatet som rå JSON istället för tabell.")
    parser.add_argument("--max-width", type=int, default=30,
                        help="Maxbredd per kolumn innan text trunkeras med '…'.")
    parser.add_argument("--no-color", action="store_true",
                        help="Inaktiverar ANSI-färger i tabellen.")
    parser.add_argument("--border", choices=["none", "ascii", "unicode", "markdown"], default="ascii",
                        help="Väljer tabellramar: ascii, unicode, markdown eller none.")
    parser.add_argument("--lang", choices=["sv", "en"], default="sv",
                        help="Språk för hjälptext (sv eller en).")

    args = parser.parse_args(argv)
    return args

def main():
    result = run(sys.argv[1:])
    print(result.output)
    return result.exit_code