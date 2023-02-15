class Ability:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage
        
    def use(self, target):
        if self.cost > target.stats.mp:
            print('Not enough MP to use this ability')
            return False
        target.stats.mp -= self.cost
        target.stats.take_damage(self.damage)
        print(f'{target.name} took {self.damage} damage from {self.name}')
        return True