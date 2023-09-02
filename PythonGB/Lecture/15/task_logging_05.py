'''
Файл журнала
До этого момента информация логгеров выводилась в консоль. Но мы можем
сохранять данные в файл, указав необходимые настройки в конфигурации.
'''

import logging
from other import log_all

logging.basicConfig(filename='project.log.', filemode='w',
encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
