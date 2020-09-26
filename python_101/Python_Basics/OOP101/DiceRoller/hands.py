from dice import D6

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("Type of die, 'die_class' arg, required.")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()
    
    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice

class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)
        
    @property
    def ones(self):
        return self._by_value(1)