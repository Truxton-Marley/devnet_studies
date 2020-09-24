import random

from characters import Character
from attributes import Agile, Sneaky

class Thief(Character, Agile, Sneaky):
    def pickpocket(self):
        return self.sneaky and random.randint(0,1)