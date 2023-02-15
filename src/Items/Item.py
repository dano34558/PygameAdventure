from Items.Abilitys import Abilities

class Item:
    def __init__(self, name, weight, value, item_type):
        self.name = name
        self.weight = weight
        self.value = value
        self.item_type = item_type

class Weapon(Item, Abilities):
    def __init__(self, name, weight, value, damage):
        super().__init__(name, weight, value, "Weapon")
        Abilities.__init__(self)
        self.damage = damage

class Armor(Item, Abilities):
    def __init__(self, name, weight, value, defense):
        super().__init__(name, weight, value, "Armor")
        Abilities.__init__(self)
        self.defense = defense

class Consumable(Item, Abilities):
    def __init__(self, name, weight, value, heal):
        super().__init__(name, weight, value, "Consumable")
        Abilities.__init__(self)
        self.heal = heal
