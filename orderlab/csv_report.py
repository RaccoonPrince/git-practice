import csv
from pathlib import Path


def revenue_from_csv(path: str | Path) -> int:
    with open(path, encoding="utf-8", newline="") as f:
        rows = csv.DictReader(f)
        return sum(int(row["price"]) * int(row["quantity"]) for row in rows)
