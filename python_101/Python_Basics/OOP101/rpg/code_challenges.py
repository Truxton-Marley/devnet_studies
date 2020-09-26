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

#######################################################

#Magic methods

"""Add a _str_ method to the DreamCar class. In the method, return a string
that states the dream car's make and model. The string should look like this:
'My dream car is a Ford Mustang.'"""

class DreamCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __str__(self):
        return f'My dream car is a {self.make} {self.model}.'

###

class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value
    
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
    
    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value
    
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other
      
    def __rmul__(self, other):
        return self * other
    
    def __imul__(self, other):
        self.value = self * other
        return self.value

###

#Iterables

class Album:
    def __init__(self):
        self.songs = []
    def add(self, song):
        self.songs.append(song)
    # insert your code here
    def __iter__(self):
        yield from self.songs

###

#Subclasses

class Double(int):
    def __new__(self, value):
        return int(value)

#Check Frustration example!!!

###

#Class Methods

"""
Below is a class called DreamVacation that holds a location and list of activities. Create a @classmethod called rome
that will return a new DreamVacation instance with cls() with the following arguments: location = 'Rome' and activities
list = ['visit the Colosseum', 'Eat gelato'].
"""

class DreamVacation:
    def __init__(self, location, activities):
        self.location = location
        self.activities = activities
    # insert your code here
    
    @classmethod
    def rome(cls):
        return cls('Rome', ['visit the Colosseum', 'Eat gelato'])


###

#Properties

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return (self.width * 2) + (self.length * 2)

###

#Just a challenge:

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))
                
class TicTacToe(Board):
    def __init__(self):
        super().__init__(3, 3) 

###

#Class comparision operators challenge:

class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length
        
    def __int__(self):
        return int(self.length)
    
    def __eq__(self, other):
        return int(self) == other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __le__(self, other):
        return int(self) <= other

    def __ge__(self, other):
        return int(self) <= other

###

#

class Hand(list):
    @property
    def total(self):
        return sum(self)
    
    @classmethod
    def roll(cls, num_die):
        hand = Hand()
        for _ in range(num_die):
            #hand.append(D20()) <--uses D20 from code challenge code;
            pass
        return hand