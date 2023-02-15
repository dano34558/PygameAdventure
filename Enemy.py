class Enemy:
    def __init__(self, name, army=None):
        self.name = name
        self.army = army or []
    
    def __str__(self):
        return self.name