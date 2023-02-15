from Items.Abilities import Abilities
import json


class Item:
    def __init__(self, name, description, value, weight, ability_names=[]):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
        self.abilities = []

        # Load the abilities from the JSON file
        with open('abilities.json') as f:
            data = json.load(f)

        # Create an instance of the Ability class for each ability in the JSON file
        for ability in data['abilities']:
            if ability['name'] in ability_names:
                self.abilities.append(Ability(ability['name'], ability['description'], ability['type']))

class Weapon(Item):
    def __init__(self, name, description, value, weight, damage, ability_names=[]):
        super().__init__(name, description, value, weight, ability_names)
        self.damage = damage

class Armor(Item):
    def __init__(self, name, description, value, weight, defense, ability_names=[]):
        super().__init__(name, description, value, weight, ability_names)
        self.defense = defense

class Consumable(Item):
    def __init__(self, name, description, value, weight, healing_amount, ability_names=[]):
        super().__init__(name, description, value, weight, ability_names)
        self.healing_amount = healing_amount
