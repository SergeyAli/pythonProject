'''
Расширение неизменяемых классов
Один из вариантов использования дандер __new__ — расширение
функциональности уже имеющихся неизменяемых классов Python. Например мы
хотим использовать переменную целого типа, которая дополнительно хранит
присвоенное числу имя.
'''

class NamedInt(int):

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance


print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
print('Создаём второй раз')
b = NamedInt(73, 'Лучшее просто число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')
