# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода.
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел.
# ✔ Добавьте аннотацию типов, где это возможно.

BINARY_DIVIDER = 2
OCT_DIVIDER = 8


def get_num_user() -> tuple[int, int]:
    info = input('Please enter a number and divider. '
                 'Use space between them:\n')
    n, d = info.split()
    return int(n), int(d)


def converter_divider(patient: int, divider: int):
    res: str = ''
    while patient > 0:
        res = str(patient % divider) + res
        patient //= divider
    return res


patient, divider = get_num_user()
if isinstance(patient, int) and divider in (BINARY_DIVIDER, OCT_DIVIDER):
    print(converter_divider(patient, divider))
else:
    print('Sth went wrong. Try again.')
