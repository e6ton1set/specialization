# Создайте в переменной data список значений разных типов, перечислив их через
# запятую, внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data = [1, 45, 'text', 2.21, False, 'text']

for i, elem in enumerate(data, start=1):
    address: int = id(elem)
    size_elem: int = sys.getsizeof(elem)
    hash_elem: int = hash(elem)
    result: str = ''

    # if isinstance (elem, int):
    if type(elem) == int:
        result = 'This is number'
    elif isinstance (elem, str):
        result = 'This is string'

    print(f'Порядковый номер элемента: {i}\n'
          f'Значение элемента: {elem}\n'
          f'Адрес в памяти: {address}\n'
          f'Размер элемента (byte): {size_elem}\n'
          f'Хэш элемента: {hash_elem}\n'
          f'Тип элемента: {result}\n'
          f'------------------------------------')