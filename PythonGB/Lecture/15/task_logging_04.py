'''
А теперь рассмотрим ситуацию с несколькими файлами, когда мы работаем сосложным проектом.
Код основного файла:
'''

import logging
from other import log_all
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
