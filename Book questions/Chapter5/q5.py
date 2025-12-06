class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def print_shape_area(shape):
    print(f"Area: {shape.area()}")

shapes = [Shape(), Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print_shape_area(shape)