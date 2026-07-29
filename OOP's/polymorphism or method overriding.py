# Polymorphism


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r**2


class Rectriangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(
        self,
    ):
        return self.l * self.b


shapes = [Circle(10), Square(20), Rectriangle(10, 20)]
for shape in shapes:
    print(shape.area())
