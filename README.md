# csv-to-json

Convert a CSV file (or piped input) to a JSON array of objects — from the terminal, no dependencies beyond Python 3.

## What it does

Reads CSV data and writes a JSON array where each row becomes an object keyed by the header names. Handles quoted fields and commas inside values.

## How to run

```bash
python3 csv_to_json.py data.csv
cat data.csv | python3 csv_to_json.py
python3 csv_to_json.py data.csv --indent 4 > data.json
python3 csv_to_json.py data.csv --output data.json
```


## Example output

Input (`people.csv`):

```csv
name,city,role
Rohit,Chandigarh,Freelancer
Asha,Mumbai,Designer
```

Command:

```bash
python3 csv_to_json.py people.csv
```

Output:

```json
[
  {
    "name": "Rohit",
    "city": "Chandigarh",
    "role": "Freelancer"
},
  {
    "name": "Asha",
    "city": "Mumbai",
    "role": "Designer"
}
]
```

## Options

| Flag | Meaning |
|------|---------|
| `input` | CSV file to read (reads from stdin if omitted) |
| `--indent N` | JSON indent spaces (default 2) |
| `--output FILE` | Write JSON to a file instead of stdout |

Exits with code 1 if the CSV has no data rows.
