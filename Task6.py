import math

class Shape:
    def __init__(self,type):
        self.type=type
        

    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def calculate_area(self):
        area = self.side**2
        print(area)


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print(area)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        print(area)



if __name__ == "__main__":
    square = Square(5)
    triangle = Triangle(3, 4)
    circle = Circle(2)
    square.calculate_area()
    triangle.calculate_area()
    circle.calculate_area()

   
