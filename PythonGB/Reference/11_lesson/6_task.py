# ------------------------------------------- 6 -----------------------------
"""
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""


class Rectangle:

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


rect1 = Rectangle(5, 10)
rect2 = Rectangle(7, 7)
rect3 = Rectangle(4, 9)

print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 != rect2: {rect1 != rect2}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")
print(f"rect1 > rect2: {rect1 > rect2}")
print(f"rect1 >= rect2: {rect1 >= rect2}")

rect_sum = rect1 + rect2
rect_diff = rect1 - rect3

print(f"Sum of rectangles: width = {rect_sum.width}, height = {rect_sum.height}")
print(f"Difference of rectangles: width = {rect_diff.width}, height = {rect_diff.height}")
