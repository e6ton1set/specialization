# Погружение в Python | Файлы и файловая система
# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random
import random as r

UPPER_BOUND = -1000
LOWER_BOUND = 1000


def fill_file(file_name='test.txt', size=1000):
    with open(file_name, mode='a', encoding='utf-8') as file:
        for _ in range(size + 1):
            first_num: int = r.randint(LOWER_BOUND, UPPER_BOUND)
            second_num: float = r.uniform(LOWER_BOUND, UPPER_BOUND).__round__(2)
            file.write(str(first_num) + '|' + str(second_num) + "\n")


fill_file()
