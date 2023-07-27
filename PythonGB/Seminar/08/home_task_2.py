'''
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов
'''

from pathlib import Path

from task_1 import text_json
from task_2 import fill_bd
from task_3 import convert_csv
from task_4 import csv_to_json
from task_6 import pickle_to_csv
from home_task_1 import direct_info


if __name__ == '__main__':
    text_json(Path('file1.txt'))
    fill_bd(Path('test_bd.json'))
    convert_csv(Path('test_bd.json'))
    csv_to_json(Path('file2.csv'), Path('file2.json'))
    pickle_to_csv(Path('json_pickle.bin'), Path('pickle_to_csv.csv'))
    direct_info(Path(r'C:\Users\Leon\PycharmProjects\pythonProject\PythonGB\Seminar\08'), 'name')



