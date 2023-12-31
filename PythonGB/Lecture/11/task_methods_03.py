'''
Умножение текста на “продвинутый текст”
методом __rmul__
Создадим класс на основе str с методом __rmul__. Если слева оказывается обычная
строка, будем между словами добавлять текст из “продвинутой строки”,
перемножим их.
'''

class StrPro(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance
    def __rmul__(self, other: str):
        words = other.split()
        result = self.join(words)
        return StrPro(result)


text = 'Каждый охотник желает знать где сидит фазан'
s = StrPro(' (=^.^=) ')
print(f'{text = }\n{s = }')
print(text * s)
print(s * text) # TypeError: 'str' object cannot be interpreted as an integer
