# Метод update
# Для расширение словаря новыми значениями используют метод update.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)

# На вход метод получает другой словарь в любой из вариаций создания словаря.
# Если передать существующий ключ, значение будет заменено новым.
# Ещё один способ создать словари из нескольких других, который появился в новой версии Python — вертикальная черта

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)

