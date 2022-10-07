import math


class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def __str__(self):
        return f"{type(self).__name__}\"s area is ==> {self.get_area()}"


class Rectangle(Shape):
    pass


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Hexagon(Square):
    def __init__(self, length):
        super().__init__(length)

    def get_area(self):
        t_sq_2 = self.length * self.length
        math_thingy = (3 * math.sqrt(3)) / 2
        area = t_sq_2 = math_thingy
        return area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)
        self.base = base
        self.height = height

    def get_area(self):
        area = self.height * self.base
        return area / 2


def main():
    pass

if __name__ == "__main__":
    main()


my_circle = Circle(9)
my_hexagon = Hexagon(4)
my_rect = Rectangle(5, 4)
my_square = Square(4)
my_triangle = Triangle(3, 2)
print(my_circle)
print(my_hexagon)
print(my_rect)
print(my_square)
print(my_triangle)

