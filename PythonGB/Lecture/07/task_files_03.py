'''
После завершения работы с файлом необходимо освободить ресурсы. Для этого
вызывается метод close().
'''

f = open('text_data.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
f.close()
