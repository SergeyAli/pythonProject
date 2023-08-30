'''
Задание №4
📌 Доработайте класс прямоугольник из прошлых семинаров.
📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
📌 Используйте декораторы свойств.
'''


class Rectangle:

    def __init__(self, height: int, width=None):
        self._height = height
        if width:
            self._width = width
        else:
            self._width = height

    def get_perimetr(self):
        return 2 * (self._height + self._width)

    def get_area(self):
        return self._width * self._height

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("должно быть больше нуля")
        self._height = value

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("должно быть больше нуля")
        self._width = value

    def __str__(self):
        return f'прямоугольник ({self._width}х{self._height}), S= {self.get_area()}'

    def __repr__(self):
        return f'размеры:({self._width}х{self._height}), S= {self.get_area()}'


if __name__ == "__main__":
    rect = Rectangle(2, 5)
    rect.width = 2

    print(rect)
