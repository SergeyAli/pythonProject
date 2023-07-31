''''
Переопределение методов
При наследовании мы можем использовать в дочернем классе все общедоступные свойства и методы родительского класса.
Кроме того можно создать свои. И если имена будут совпадать, произойдёт переопределение.
Будут браться значения дочернего класса.
'''

class Person:
    ...


class Hero(Person):


    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)


    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2


    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
p2 = Person('Маг', 'Тролль')
print(f'{p1.health = }, {p2.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }')
p2.change_health(p1, 10)
print(f'{p1.health = }, {p2.health = }')
p1.add_many_up()
print(f'{p1.up = }')


