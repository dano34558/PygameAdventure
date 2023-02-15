import json

class Ability:
    def __init__(self, name, description, ability_type):
        self.name = name
        self.description = description
        self.type = ability_type

# Load the abilities from the JSON file
with open('abilities.json') as f:
    data = json.load(f)

# Create an instance of the Ability class for each ability in the JSON file
abilities = []
for ability in data['abilities']:
    abilities.append(Ability(ability['name'], ability['description'], ability['type']))