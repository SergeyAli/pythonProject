'''
5. Модуль argparse
Он генерирует справку, определяет способ анализа аргументов командной строки, сообщает об ошибках и даёт подсказки.
Чтобы разобраться во всём перечисленном по традиции рассмотрим простой пример.
'''

import argparse
parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float,
nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

"""
Примеры запуска в терминале:
python .\task_argparse_01.py 42 3.14 73
python .\task_argparse_01.py --help
python .\task_argparse_01.py Hello world!
"""

