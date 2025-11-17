import json
import csv
import yaml
from pathlib import Path


def load_json(path):
    with open(Path(path), "r") as f:
        return json.load(f)


def load_yaml(path):
    with open(Path(path), "r") as f:
        return yaml.safe_load(f)


def load_csv(path):
    with open(Path(path), newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
