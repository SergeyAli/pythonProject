'''
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
'''
from task_4 import create_file_

def create_dif_files (**kwargs):
    for ext, num in kwargs.items():
        create_file_(ext, count_file=num)


if __name__=='__main__':
    create_dif_files(txt=2, bin=4, png=8)