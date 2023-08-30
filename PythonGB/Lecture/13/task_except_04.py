'''
● Несколько except для одного try
Как вы уже догадались при вводе нуля в примерах на деление выше мы получим ошибку.
Это ZeroDivisionError: division by zero. Вспомним высшую математику, а именно то, что при делении любого числа на ноль
получаем бесконечность.
'''

def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            div = 100 / num
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n' f'Попробуйте снова')
        except ZeroDivisionError as e:
            div = float('inf')
            break
    return num, div


if __name__ == '__main__':
    n, d = hundred_div_num('Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')
