# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы,
# которые не подошли для сортировки

from string import ascii_lowercase, digits
from random import choices, randint
from os import path
import os


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


def sort_files_by_directories():
    for file in os.listdir():
        extention = file.split('.')[-1]
        if not os.path.exists(extention):
            if extention in 'py':
                continue
            else:
                os.mkdir(extention)

        os.replace(file, os.path.join(os.getcwd(), extention, file))


make_exp(mp3=3, avi=2, txt=1)
sort_files_by_directories()