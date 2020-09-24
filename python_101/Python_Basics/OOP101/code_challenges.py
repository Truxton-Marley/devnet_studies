#######################################################

#Basic Class creation challenge

class RaceCar():
    laps = 0
    
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps += 1

#######################################################

#Inheritance, super() code challenge:

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.slots.sort()