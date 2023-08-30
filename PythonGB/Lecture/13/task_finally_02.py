'''
Блок finally без except
Вполне допустимо использовать только связку try-finally. Например мы хотим
прочитать информацию из файла. И независимо от результат чтения закрыть его.
'''

file = open('text.txt', 'r', encoding='utf-8')
try:
    data = file.read().split()
    print(data[len(data)])
finally:
    print('Закрываю файл')
file.close()
