# Dunder method
# __str__ and __repr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"Point(x={self.x},y={self.y})"


p = Point(3, 4)
print(p)  # here instead of p.__str__() we shortend with dunder

print(repr(p))
