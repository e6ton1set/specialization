# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке (100-1000 строк).
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
from random import randint, uniform


def gen_rnd_float_cvs(file_path: str, min_row: int = 100, max_row: int = 1000,
                      min_float: float = -100.0, max_float: float = 100) -> None:
    with open(file_path, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(randint(min_row, max_row)):
            csv_writer.writerow(uniform(min_float, max_float) for _ in range(3))


def find_quadratic_sqrt(a: float, b: float, c: float) -> tuple:
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        d = complex(d, 0)
        return str((-b + d ** 0.5) / (2 * a))[1:-1], str((-b - d ** 0.5) / (2 * a))[1:-1]


if __name__ == '__main__':
    gen_rnd_float_cvs('rnd_nums.cvs')
