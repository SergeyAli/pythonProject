# ------------------------------------------- 6 -----------------------------
# Добавьте в модуль с загадками функцию,
# которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.

# Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

_data = {}

def save(puzzle: str, count: int):
    _data.update({puzzle: count})


def show():
    res = (f'Загадку "{key}" разгадали с {value}-й попытки' if value > 0
           else f'Загадку "{key}" не разгадали'
           for key, value in _data.items())
    print('\n'.join(res))
