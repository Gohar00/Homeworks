class ValidType:
    def __init__(self, type_):
        self.type_ = type_

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise ValueError(f"Expected type {self.type_.__name__}, but got {type(value).__name__}.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Int(ValidType):
    def __init__(self):
        super().__init__(int)


class Float(ValidType):
    def __init__(self):
        super().__init__(float)


class List(ValidType):
    def __init__(self):
        super().__init__(list)


class Person:
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()
    name = ValidType(str)  # For a string, we use ValidType directly

    def __init__(self, age, height, tags, favorite_foods, name):
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods
        self.name = name

try:
    person = Person(25, 6.1, ["friendly", "funny"], ["pizza", "ice cream"], "Mark")
    print(person.age)
    print(person.height)
    print(person.tags)
    print(person.favorite_foods)
    print(person.name)

    # Trying to assign incorrect types will raise ValueErrors
    person.age = "twenty-five"
    person.height = "six feet"
    person.tags = "friendly"
    person.favorite_foods = ("sushi", "ramen")
    person.name = 123
except ValueError as e:
    print(f"Error: {e}")