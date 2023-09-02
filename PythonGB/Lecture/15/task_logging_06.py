'''
Формат сохранения события
Кроме того для базовой конфигурации используют параметр format для изменения стандартной строки логирования.
Рассмотрим стил с фигурными скобками как наиболее привычный современным
разработчикам. Кстати, сам стиль надо указать при вызове конфигуратора в
параметре style.
'''

import logging
from other import log_all
FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger('main')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
