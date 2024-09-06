import json

# JSON data as a string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_data)

print(python_dict)
