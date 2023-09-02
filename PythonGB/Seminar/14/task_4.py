'''
Задание №4
📌 Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

from task_2 import deleter_simbols
import pytest

def test_no_ch():
    assert deleter_simbols('hello world') == 'hello world'
def test_Title():
    assert deleter_simbols('Hello World') == 'hello world'
def test_delete_symbols():
    assert deleter_simbols('Hello, World!') == 'hello world'
def test_delete_rus():
    assert deleter_simbols('Hello wяrld') == 'hello wrld'
def test_all():
    assert deleter_simbols('Hello%, Wяr&ld!') == 'hello wrld'

if __name__ == '__main__':
    pytest.main(['-v'])
