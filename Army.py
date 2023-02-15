from Soldier import Soldier

class Army:
    def __init__(self, name, soldiers=None):
        self.name = name
        self.soldiers = soldiers or []
    
    def add_soldier(self, soldier):
        self.soldiers.append(soldier)
    
    def remove_soldier(self, soldier):
        self.soldiers.remove(soldier)
    
    def get_soldier(self, soldier_type):
        for soldier in self.soldiers:
            if soldier.soldier_type == soldier_type:
                return soldier
        return None
    
    def get_army_size(self):
        return len(self.soldiers)
    
    def __str__(self):
        return f"{self.name} (size {self.get_army_size()})"