from typing import List, Dict
from utils.normalize import normalize_headers


def parse_csv_file(filepath: str) -> List[Dict]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    headers = normalize_headers(lines[0].strip().split(","))
    data = []

    for line in lines[1:]:
        values = line.strip().split(",")
        row = dict(zip(headers, values))
        data.append(row)

    return data


def parse_csv_files(files: List[str]) -> List[Dict]:
    result = []
    for file in files:
        result.extend(parse_csv_file(file))
    return result
