class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(f"Point created: {p}")
print(f"x = {p.x}, y = {p.y}")

p.z = 5 # will return an error