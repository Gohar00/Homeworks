class TypeCheckingMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith("__"):
                attr_type = attrs.get(f"_{attr_name}_type", None)
                if attr_type:
                    setattr(cls, attr_name, TypeCheckingMeta._create_property(attr_name, attr_type))

    @staticmethod
    def _create_property(attr_name, attr_type):
        def getter(self):
            return getattr(self, f"_{attr_name}")

        def setter(self, value):
            if not isinstance(value, attr_type):
                raise TypeError(f"Attribute '{attr_name}' must be of type {attr_type.__name__}")
            setattr(self, f"_{attr_name}", value)

        return property(getter, setter)


class Person(metaclass=TypeCheckingMeta):
    _name_type = str
    _age_type = int
    _height_type = float

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height



if __name__ == "__main__":

    person1 = Person("Alice", 30, 1.65)
    print(person1.name)   
    print(person1.age)     
    print(person1.height)  


    try:
        person1.name = 123  
    except TypeError as e:
        print(e)

    try:
        person1.age = "30"  
    except TypeError as e:
        print(e)

    try:
        person1.height = "1.65" 
    except TypeError as e:
        print(e)p
