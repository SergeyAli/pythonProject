'''
Для изменения текущего каталога можно воспользоваться функцией os.chdir.
Она принимает на вход абсолютный или относительный путь до нового текущего каталога.
'''

import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())
