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

from string import ascii_lowercase, digits
from random import choices, randint


def make_files(exp: str, min_name_len: int = 6, max_name_len: int = 30,
               min_size: int = 256, max_size: int = 4096, amount: int = 42) -> None:

    for _ in range(amount):
        name = ''.join(choices(ascii_lowercase+ digits + '_', k=randint(min_name_len, max_name_len)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))

        with open(rf'task_4\{name}.{exp}', mode='wb') as rnd_files:
            rnd_files.write(data)


make_files(exp="txt")