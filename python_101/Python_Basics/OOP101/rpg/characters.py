class Character:
    def __init__(self, name="", **kwargs):
        if not name:
            raise ValueError("Name is required.")
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"
