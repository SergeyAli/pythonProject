'''
Задание №1
📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
📌 Экземпляр должен запоминать последние k значений.
📌 Параметр k передаётся при создании экземпляра.
📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
'''

from collections import deque


class Factorial:

    def __init__(self, count):
        self.count = count
        self.archive = deque(maxlen=count)

    def __call__(self, number):
        res = 1
        for item in range(1, number + 1):
            res *= item
        self.archive.append((number, res))
        return res

    def __str__(self):
        return str(self.archive)


if __name__ == "__main__":
    factor = Factorial(3)
    print(factor(5))
    print(factor(2))
    print(factor(3))
    factor(6)
    factor(2)

    print(factor)
