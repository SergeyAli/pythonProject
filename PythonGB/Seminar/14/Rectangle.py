'''

'''
class Rectangle:

    def __init__ (self, side_a: float, side_b: float | None = None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self) -> float:
        return 2 * (self._side_a + self._side_b)

    def get_area(self) -> float:
        return self._side_a * self._side_b  # вызывает property c length и возвращает _length

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __str__(self):
        return f'Rectangle({self._side_a}, {self._side_b})' \
               f'\nPerimetr {self.get_perimeter()}' \
               f'\nArea {self.get_area()}'

    def __repr__(self):
        return f'Rectangle({self._side_a, self._side_b})'

if __name__ == '__main__':
    a = Rectangle(3, 7) - Rectangle(2, 5)
    b = Rectangle(1, 2)
    print(a)
    print(b)
