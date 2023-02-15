class Soldier:
    def __init__(self, soldier_type, army_size, health, level):
        self.soldier_type = soldier_type
        self.army_size = army_size
        self.health = health
        self.level = level
        
    def __str__(self):
        return f"{self.soldier_type} (level {self.level}, health {self.health}, army size {self.army_size})"