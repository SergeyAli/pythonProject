'''
При вызове функции print сработал метод __str__. Как же получить вывод от
__repr__ при наличии двух методов? Есть несколько способов вывода на печать:
'''

class User:

    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'

user = User('Венкман', ['протонный ускоритель', 'ловушка'])
print(user)
print(f'{user}')
print(repr(user))
print(f'{user = }')
