import json

# Write JSON
person = {
    "name": "Divya",
    "age": 20,
    "city": "Bangalore",
    "hobbies": ["coding", "reading", "music"]
}

with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

print("✅ JSON file write aythu!\n")

# Read JSON
with open("person.json", "r") as f:
    data = json.load(f)

print(f"👤 Name: {data['name']}")
print(f"🎂 Age: {data['age']}")
print(f"🏙️ City: {data['city']}")
print(f"🎯 Hobbies: {', '.join(data['hobbies'])}")
