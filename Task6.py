import math

class Shape:
    def __init__(self):
        self.area = 0

    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calculate_area(self):
        self.area = self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_area(self):
        self.area = 0.5 * self.base * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        self.area = math.pi * self.radius * self.radius


def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        shape.calculate_area()
        total_area += shape.area
    return total_area


if __name__ == "__main__":
    square = Square(5)
    triangle = Triangle(3, 4)
    circle = Circle(2)

    shapes = [square, triangle, circle]
    total_area = calculate_total_area(shapes)

    print("Total area:", total_area)