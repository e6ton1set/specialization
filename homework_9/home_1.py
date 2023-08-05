# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл

import cmath
import csv
import random
from functools import wraps
from typing import Callable

SIZE = 100
UPPER_LIMIT = 100
LOWER_LIMIT = 1


def deco_from_find_quadratic_roots(func: Callable[[float], float]) -> Callable[[str], list[dict]]:
    @wraps(func)
    def wrapper(csv_file_path: str) -> list[dict]:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)

            result = []
            for params in csv_reader:
                if params != '':
                    cur_result = {
                        'params': params,
                        'result': func(*params)
                    }
                result.append(cur_result)

            return result

    return wrapper


@deco_from_find_quadratic_roots
def find_quadratic_roots(a, b, c: any) -> tuple:
    d = (b ** 2) - (4 * a * c)
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)

    return x1, x2


def create_rnd_cvs(cvs_path: str) -> None:
    rows = []
    for _ in range(SIZE):
        num1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        num2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        num3 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        rows.append({'num1': num1, 'num2': num2, 'num3': num3})

    with open(cvs_path, 'w', encoding='utf-8') as csv_file:
        three_rnd_nums = csv.DictWriter(csv_file, fieldnames=['num1', 'num2', 'num3'], dialect='excel')
        three_rnd_nums.writeheader()
        three_rnd_nums.writerows(rows)


if __name__ == '__main__':
    print(deco_from_find_quadratic_roots("rnd_nums.csv"))
