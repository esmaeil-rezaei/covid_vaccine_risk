import csv
import json

# Read CSV file
with open('artifacts/data.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Write to JSON file
with open('data.json', mode='w') as json_file:
    json.dump(data, json_file, indent=4)
