#!/usr/bin/env python3
"""csv-to-json: convert a CSV file (or stdin) to JSON.

Reads a CSV and writes a JSON array of row objects to stdout.
stdin/stdout friendly, so it slots into shell pipelines.

Usage:
    python3 csv_to_json.py data.csv
    cat data.csv | python3 csv_to_json.py
    python3 csv_to_json.py data.csv --indent 4 > data.json
    python3 csv_to_json.py data.csv --output data.json
"""

import argparse
import csv
import json
import sys


def csv_to_records(text):
    reader = csv.DictReader(text.splitlines())
    return [row for row in reader]


def main():
    parser = argparse.ArgumentParser(description="Convert CSV to a JSON array of objects.")
    parser.add_argument("input", nargs="?", help="CSV file (reads stdin if omitted)")
    parser.add_argument("--indent", type=int, default=2, help="JSON indent (default 2)")
    parser.add_argument("--output", help="Write JSON to this file instead of stdout")
    args = parser.parse_args()

    if args.input:
        with open(args.input, newline="", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    records = csv_to_records(text)
    if not records:
        print("Error: no data rows found in the CSV.", file=sys.stderr)
        sys.exit(1)

    output = json.dumps(records, indent=args.indent, ensure_ascii=False) + "\n"

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
