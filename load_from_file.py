import json

# Open a JSON file and load its contents
with open('dictionary.json', 'r') as file:
    python_dict = json.load(file)

print(python_dict)
