class Int:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value must be greater than or equal to {self.min_value}.")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Value must be less than or equal to {self.max_value}.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Point2D:
    x = Int(min_value=0)
    y = Int(min_value=0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point2DSequence:
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __set__(self, instance, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError("Value must be a sequence (list or tuple) of Point2D instances.")
        for point in value:
            if not isinstance(point, Point2D):
                raise ValueError("Each element in the sequence must be an instance of Point2D.")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"The sequence must have at least {self.min_length} vertices.")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"The sequence must have at most {self.max_length} vertices.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Polygon:
    vertices = Point2DSequence(min_length=3, max_length=10)

    def __init__(self, *vertices):
        self.vertices = list(vertices)

    def append(self, point):
        if len(self.vertices) < Polygon.vertices.max_length:
            if not isinstance(point, Point2D):
                raise ValueError("Appended value must be an instance of Point2D.")
            self.vertices.append(point)
        else:
            raise ValueError("Cannot append more vertices, maximum length reached.")

try:
    p1 = Point2D(0, 0)
    p2 = Point2D(4, 0)
    p3 = Point2D(2, 3)
    p4 = Point2D(1, 1)  # Additional point for testing append method

    poly = Polygon(p1, p2, p3)
    print(poly.vertices)

    # Test appending a new point
    poly.append(p4)
    print(poly.vertices)
    # Trying to append more than the maximum allowed vertices
    p5 = Point2D(5, 5)
    p6 = Point2D(6, 6)
    poly.append(p5)
    poly.append(p6)  # Raises ValueError: Cannot append more vertices, maximum length reached.

    # Trying to assign incorrect types to 'vertices' attribute
    poly.vertices = (p1, p2, "invalid")
except ValueError as e:
    print(f"Error: {e}")
