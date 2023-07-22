'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

from sys import argv

def _check_leap_year(year):
    return not year % 4 != 0 or year % 100 != 0 or year % 400 != 0


def task_date(date: str):
    day, month, year = map(int, date.split('.'))
    if not 0 < year < 10000 or not 0 < month < 13 or not 0 < day < 32:
        return False
    if month not in [4, 6, 9, 11] and day > 30:
        return False

    leap = _check_leap_year(year)
    if leap and month == 2 and day > 29:
        return False
    if not leap and month == 2 and day > 28:
        return False
    return True


max_day = 0

_, *param = argv

print(task_date(*param))