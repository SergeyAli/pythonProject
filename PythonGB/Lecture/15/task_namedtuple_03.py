'''
При создании класса можно дополнительно передать список значений по умолчанию. И если дефолтных значений меньше,
чем свойств в классе, назначение происходит справа налево
'''

import time
from collections import namedtuple
from datetime import datetime

SECONDS = 7
User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
print(f'пауза в {SECONDS} секунд...')
time.sleep(SECONDS)
u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
