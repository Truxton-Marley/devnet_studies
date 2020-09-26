import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("\nThe die must have at least two sides.\n")
        if not isinstance(sides, int):
            raise ValueError("\nSides is required to be a whole number!!!\n")
        self.value = value or random.randint(int, sides)

class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
    
    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D20(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
    
    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)
