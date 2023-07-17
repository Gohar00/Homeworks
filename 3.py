class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        return "Engine started."

    def stop(self):
        return "Engine stopped."


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start(self):
        return f"{self.brand} {self.model} with {self.num_doors} doors: Engine started."

    def stop(self):
        return f"{self.brand} {self.model} with {self.num_doors} doors: Engine stopped."


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, num_wheels):
        super().__init__(brand, model, year)
        self.num_wheels = num_wheels

    def start(self):
        return f"{self.brand} {self.model} with {self.num_wheels} wheels: Engine started."

    def stop(self):
        return f"{self.brand} {self.model} with {self.num_wheels} wheels: Engine stopped."


class Bicycle(Vehicle):
    def __init__(self, brand, model, year, num_gears):
        super().__init__(brand, model, year)
        self.num_gears = num_gears

    def start(self):
        return f"{self.brand} {self.model} with {self.num_gears} gears: Pedaling started."

    def stop(self):
        return f"{self.brand} {self.model} with {self.num_gears} gears: Pedaling stopped."



