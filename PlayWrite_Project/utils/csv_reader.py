# utils/csv_reader.py
# Helper utility to read username and password from a CSV file.

import csv

def get_csv_data(file_path):
    """Reads username and password from CSV file and returns a list of tuples."""
    data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row["username"], row["password"]))
    return data
