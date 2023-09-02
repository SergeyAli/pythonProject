'''
Задание №5
📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр, площадь и
позволяющий складывать и вычитать прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса.
'''

from builtins import str

from Rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

    def test_1_area(self):
        self.assertEqual(Rectangle.get_area(Rectangle(2)), 4)
    def test_2_perimetr(self):
        self.assertEqual(Rectangle.get_perimeter(Rectangle(2,5)), 14)
    def test_2_sub(self):
        self.assertEqual(str(Rectangle(3, 7) - Rectangle(2, 5)), str(Rectangle(1, 2)))
    def test_2_sum(self):
        self.assertEqual(str(Rectangle(3, 7) + Rectangle(2, 5)), str(Rectangle(5, 12)))


if __name__ == '__main__':
    unittest.main(verbosity=2)

