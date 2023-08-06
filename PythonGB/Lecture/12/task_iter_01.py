'''
2. Создаём итераторы
Создадим класс экземпляр которого будет выдавать числа Фибоначчи в диапазоне
начиная с числа больше или равного start и заканчивая числом меньше stop.
'''

class Fibonacci:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

fib = Fibonacci(20, 100)
for num in fib: # TypeError: 'Fibonacci' object is not iterable
    print(num)
