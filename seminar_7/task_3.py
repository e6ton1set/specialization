# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from typing import TextIO

__all__ = ['read_file']

def readline_or_begin(file: TextIO) -> str:
    line = file.readline()

    if line == '':
        file.seek(0)
        line = file.readline()

    return line[:-1]


def read_file():
    with (
        open('test.txt', encoding='utf-8') as nums_file,
        open('names.txt', encoding='utf-8') as names_file,
        open('result.txt', mode='w', encoding='utf-8') as res_file
    ):
        len_names = len(names_file.readlines())
        len_nums = len(nums_file.readlines())

        for _ in range(max(len_nums, len_names)):
            curr_name = readline_or_begin(names_file)
            curr_num = readline_or_begin(nums_file)
            a, b = curr_num.split('|')
            temp = int(a) * float(b)
            if temp > 0:
                res_file.write(curr_name.upper() + '\t' + str(round(temp, 2)) + '\n')
            else:
                res_file.write(curr_name.lower() + '\t' + str(-temp) + '\n')


if __name__ == '__main__':
    read_file()