'''
Фикстуры pytest как замены unittest setUp и tearDown
Если вам необходимо выполнить однотипные действия для подготовки нескольких тестов, можно создать собственные фикстуры.
Рассмотрим простой пример из главы о unittest.
'''

import pytest

@pytest.fixture

def data():
    return [2, 3, 5, 7]

def test_append(data):
    data.append(11)
    assert data == [2, 3, 5, 7, 11]

def test_remove(data):
    data.remove(5)
    assert data == [2, 3, 7]

def test_pop(data):
    data.pop()
    assert data == [2, 3, 5]

if __name__ == '__main__':
    pytest.main(['-v'])
