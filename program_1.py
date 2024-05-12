import json

# Load the data from the input file
with open('pl-PL.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a new dictionary to hold the transformed data
new_data = {}

# Iterate over the keys and values in the input dictionary
for key, value in data.items():
    # Split the key on the '.' character
    parts = key.split('.')
    
    # Check if the key contains at least two '.' characters
    if len(parts) < 3:
        continue

    # Get the location and role
    location, role = parts[1:]

    # Check if the location is already in the new dictionary
    if location not in new_data:
        # If it's not, add it with an empty dictionary as its value
        new_data[location] = {}

    # Check if the role starts with 'role'
    if role.startswith('role'):
        # If it does, add it to the dictionary for the current location
        new_data[location][role] = value
    else:
        # If it doesn't, add it as the 'name' for the current location
        new_data[location]['name'] = value

# Write the new dictionary to the output file in JSON format
with open('spyfall_dictionary.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)