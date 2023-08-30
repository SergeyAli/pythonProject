# ------------------------------------------- 2 -----------------------------
"""
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from string import ascii_letters


def filter_lower(s: str) -> str:
    """
    >>> filter_lower('hi bro')
    'hi bro'
    >>> filter_lower('Hello world')
    'hello world'
    >>> filter_lower('hello, my friend!')
    'hello my friend'
    >>> filter_lower('привет переводится как hello')
    '   hello'
    >>> filter_lower('Hello, мой дорогой друг Jony!')
    'hello    jony'
    """
    result = ''.join(char for char in s if char in set(ascii_letters + ' '))
    return result.lower().strip(' ')


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
