from Soldier import Soldier

class Player:
    def __init__(self, name, location, inventory=None, army=None):
        self.name = name
        self.location = location
        self.inventory = inventory or []
        self.army = army or []
        self.gold = 0
        self.experience = 0
        self.level = 1
    
    def move(self, x, y):
        self.location = (x, y)
    
    def gather_resources(self, resource_type, amount):
        if resource_type in self.inventory:
            self.inventory[resource_type] += amount
        else:
            self.inventory[resource_type] = amount
    
    def battle(self, enemy):
        enemy_army_size = sum(soldier.army_size for soldier in enemy.army)
        player_army_size = sum(soldier[1] for soldier in self.army)
        
        if player_army_size > enemy_army_size:
            for i, soldier in enumerate(self.army):
                if soldier[1] >= enemy_army_size:
                    self.army[i] = (soldier[0], soldier[1] - enemy_army_size)
                    enemy.army = []
                    break
                else:
                    enemy_army_size -= soldier[1]
                    self.army[i] = (soldier[0], 0)
            return True
        else:
            self.army = []
            return False
        
