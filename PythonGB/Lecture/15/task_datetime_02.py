'''
Разница времени
Ещё один важный тип данных — timedelta. Объект представляет из себя разницу во времени между различными датами и
временными промежутками.
Простой пример создания временной разницы:
'''

from datetime import timedelta
delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)
print(f'{delta = }\t-\t{delta}')
