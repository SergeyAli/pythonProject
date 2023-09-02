'''
3. Модуль datetime
Ещё один полезный модуль — datetime. Как понятно из названия он необходим для обработки даты и времени.
Создаём дату и время
Следующий пример демонстрирует три основных типа данных модуля.
'''

from datetime import time, date, datetime
d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, second=0, microsecond=24)
print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{dt = }\t-\t{dt}')
