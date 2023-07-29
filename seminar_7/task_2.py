# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random


def get_rnd_name():
    vowels = "ауеиоуыэюя"
    consonants = "бвгджзклмнпртсфчхшщ"

    def gen_name(code):
        return "".join((random.choice(vowels if char == '0' else consonants) for char in code))

    codes = ['0', '1', '01', '10', '010', '101']
    types = [gen_name(code) for code in codes]

    return ''.join(random.sample(types, 3))


print(get_rnd_name() if 4 < len(get_rnd_name()) < 7 else 'Неудачная попытка генерации')
