# Функция может принять лишь один аргумент. В случае со списком проблем нет.
# Но если перечислить элементы через запятую и не указать скобки - не передать кортеж, получим ошибку.
def mean(*args):
    return sum(args) / len(args)

print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))