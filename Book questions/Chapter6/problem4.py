import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = {"people": [row for row in reader]}
    
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"Converted {csv_file} to {json_file}")

csv_to_json("people.csv", "people.json")
