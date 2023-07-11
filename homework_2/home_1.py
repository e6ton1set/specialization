# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

BINARY_DIVIDER: int = 2
OCT_DIVIDER: int = 8
HEX_DIVIDER: int = 16
list_hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']


def enter_num_user() -> tuple[int, int]:
    try:
        info = input('Введите число и систему счисления через пробел:\n')
        divis, div = info.split()
        return int(divis), int(div)
    except:
        print('Ошибка ввода. Возможно, вы забыли поставить пробел.')


def converter_divider(divisible: int, divider: int) -> str:
    res: str = ''
    if divider in (BINARY_DIVIDER, OCT_DIVIDER):
        while divisible != 0:
            res = res + str(divisible % divider)
            divisible //= divider
        rev_res = res[::-1]
    else:
        while divisible != 0:
            temp = divisible % divider
            res += str(list_hex[temp])
            divisible //= divider
        rev_res = res[::-1]
    return rev_res


divisible, divider = enter_num_user()
if isinstance(divisible, int) and divider in \
        (BINARY_DIVIDER, OCT_DIVIDER, HEX_DIVIDER):
    res = converter_divider(divisible, divider)
    print(f'Вы выбрали {divider}-ю систему счисления.\n'
        f'Число {divisible} успешно конвертировано.\n'
        f'Результат: {res}')
else:
    print('Произошла ошибка. Запустите программу повторно.')

print(f'__________________________________________________________\n'
      f'Проверка: число {divisible} в 2, 8, 16 системах счисления:\n'
      f'{bin(divisible)[2:]}\n'
      f'{oct(divisible)[2:]}\n'
      f'{hex(divisible)[2:]}')


