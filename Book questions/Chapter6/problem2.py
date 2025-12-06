import json

data = {
    "course": "Python",
    "duration": "3 months",
    "students": ["Ali", "Sara"]
}

with open('course.json', 'w') as file:
    json.dump(data, file, indent=2)

with open('course.json', 'r') as file:
    loaded_data = json.load(file)
    print("Students:", loaded_data['students'])