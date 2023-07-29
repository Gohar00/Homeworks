class SlottedStruct(type):
    def new(cls, name, bases, namespace):
        slots = namespace.get('slots', ())
        if not isinstance(slots, tuple):
            raise TypeError("'slots' attribute must be a tuple.")
        namespace['slots'] = slots
        return super().new(cls, name, bases, namespace)

    def init(cls, name, bases, namespace):
        super().init(name, bases, namespace)

        def init(self, *args):
            if len(args) != len(self.slots):
                raise TypeError(f'{name} expected {len(self.slots)} arguments, got {len(args)}')
            for slot, value in zip(self.slots, args):
                setattr(self, slot, value)

        def eq(self, other):
            if not isinstance(other, cls):
                return False
            return all(getattr(self, slot) == getattr(other, slot) for slot in self.slots)

        def hash(self):
            return hash(tuple(getattr(self, slot) for slot in self.slots))

        def repr(self):
            args_str = ', '.join(repr(getattr(self, slot)) for slot in self.slots)
            return f'{name}({args_str})'

        def str(self):
            args_str = ', '.join(str(getattr(self, slot)) for slot in self.slots)
            return f'({args_str})'

        cls.init = init
        cls.eq = eq
        cls.hash = hash
        cls.repr = repr
        cls.str = str

class Point2D(metaclass=SlottedStruct):
    slots = ('_x', '_y')

class Point3D(metaclass=SlottedStruct):
    slots = ('_x', '_y', '_z')


p2d_1 = Point2D(1, 2)
p2d_2 = Point2D(3, 4)

print(p2d_1)
print(p2d_1 == p2d_2)
print(hash(p2d_1))
print(repr(p2d_1))


p3d_1 = Point3D(1, 2, 3)
p3d_2 = Point3D(1, 2, 3)

print(p3d_1)
print(p3d_1 == p3d_2)
print(hash(p3d_1))
print(repr(p3d_1))


p4d_1 = Point4D(1, 2, 3, 4)
p4d_2 = Point4D(5, 6, 7, 8)

print(p4d_1)
print(p4d_1 == p4d_2)
print(hash(p4d_1))
print(repr(p4d_1))