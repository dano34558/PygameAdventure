class Stats:
    def __init__(self, hp, mp, strength, defense, agility):
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.defense = defense
        self.agility = agility
        
    def take_damage(self, damage):
        self.hp -= damage
        
    def heal(self, amount):
        self.hp += amount
        
    def is_alive(self):
        return self.hp > 0