# ------------------------------------------- 1 -----------------------------
"""
📌 Создайте функцию, которая удаляет из текста все символы
    кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре.
"""


def clean_text(text):
    cleaned_chars = [char for char in text if char.isalpha() or char.isspace()]
    cleaned_text = ''.join(cleaned_chars).lower()
    return cleaned_text


cleaned_output = clean_text("Пример 123 текста с @символами на русском языке!")
print(cleaned_output)