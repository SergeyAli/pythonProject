'''
В документации есть несколько примеров, имитирующих работу в режиме
интерпретатора. Убедимся, что они рабочие, написав в отдельном файле пару строк
кода.
'''

import doctest
doctest.testfile('prime.md', verbose=True)
