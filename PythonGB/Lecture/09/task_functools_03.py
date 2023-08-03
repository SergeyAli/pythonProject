'''
Декоратор cache
Рассматривая возможности по замыканию переменных мы создали кэширующий декоратор. В модуле functools есть
декоратор cache с подобным функционалом. При необходимости кэширования данных рекомендуется использовать именно его,
как более оптимальное решение из коробки.
'''

from functools import cache

@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
