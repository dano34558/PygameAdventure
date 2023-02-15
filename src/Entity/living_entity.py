from Entity.entity import Entity
from Entity.utility.Stats import Stats
from Entity.utility.abilitys import Ability

class LivingEntity(Entity):
    def __init__(self, name, stats, abilities):
        super().__init__(name=name, entity_type='living')
        self.stats = stats
        self.abilities = abilities
        
    def use_ability(self, ability, target):
        if ability.cost > self.stats.mp:
            print('Not enough MP to use this ability')
            return False
        self.stats.mp -= ability.cost
        target.stats.take_damage(ability.damage)
        print(f'{target.name} took {ability.damage} damage from {ability.name}')
        return True