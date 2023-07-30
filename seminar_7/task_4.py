# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from string import ascii_lowercase, digits
from random import choices, randint
from os import path
import os

__all__ = ['make_exp', 'make_files']

def check_dir(dir, **kwargs) -> None:
    if not path.exists(dir):
        os.mkdir(dir)

    os.chdir(dir)
    make_exp(**kwargs)


def make_files(exp: str, min_name_len: int = 6, max_name_len: int = 30,
               min_size: int = 256, max_size: int = 4096, amount: int = 42) -> None:
    for _ in range(amount):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name_len, max_name_len)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(rf'{name}.{exp}', mode='wb') as rnd_files:
            rnd_files.write(data)


def make_exp(**kwargs):
    for exp, amount in kwargs.items():
        make_files(exp=exp, amount=amount)


if __name__ == '__main__':
    check_dir(r'.\\task_6', png=2, pdf=1)
