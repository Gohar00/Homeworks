class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Hundred(metaclass=SingletonMeta):
    def __init__(self):
        setattr(self, 'name', 'hundred')
        setattr(self, 'value', 100)

h1 = Hundred()
h2 = Hundred()
print(h1 is h2) 
print(vars(h1))
print(vars(h2))