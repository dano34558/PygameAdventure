import random

class EventManager:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def run_event(self):
        event_type = random.choice(['item', 'battle'])
        if event_type == 'item':
            self._generate_item_event()
        elif event_type == 'battle':
            self._generate_battle_event()
    
    def _generate_item_event(self):
        item_types = ['sword', 'shield', 'potion', 'gold']
        item_type = random.choice(item_types)
        if item_type == 'gold':
            amount = random.randint(1, 10) * 10
            print(f"You found {amount} gold!")
            self.player.gold += amount
        else:
            print(f"You found a {item_type}!")
            self.player.inventory.append(item_type)
    
    def _generate_battle_event(self):
        print("You encountered an enemy army!")
        print(f"{self.enemy.name} (size {self.enemy.army.get_army_size()})")
        
        while self.player.army and self.enemy.army:
            player_soldier = random.choice(self.player.army)
            enemy_soldier = random.choice(self.enemy.army)
            
            # Player attacks first
            enemy_soldier.health -= player_soldier.damage
            print(f"{player_soldier} attacks {enemy_soldier} for {player_soldier.damage} damage!")
            if enemy_soldier.health <= 0:
                self.enemy.remove_soldier(enemy_soldier)
                print(f"{enemy_soldier} has been defeated!")
            
            # Enemy attacks next
            if self.enemy.army:
                player_soldier = random.choice(self.player.army)
                player_soldier.health -= enemy_soldier.damage
                print(f"{enemy_soldier} attacks {player_soldier} for {enemy_soldier.damage} damage!")
                if player_soldier.health <= 0:
                    self.player.remove_soldier(player_soldier)
                    print(f"{player_soldier} has been defeated!")
        
        if self.player.army:
            print("You won the battle!")
            self.player.experience += 100
        else:
            print("You lost the battle!")