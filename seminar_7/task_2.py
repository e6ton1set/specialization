# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random


def generate_name():
    vowels = "аууееиоуыэюя"
    consonants = "бвгджзклмнпртсфчхшщ"

    def gen_type(code):
        return "".join((random.choice(vowels if c == '0' else consonants) for c in code))

    codes = ['0', '1', '01', '10', '010', '101']
    types = [gen_type(code) for code in codes]

    return ''.join(random.sample(types, 3))


def validate_name():
    while True:
        name = generate_name()
        if 4 < len(name) < 7:
            break
    return name


def fill_file(file_name="names.txt", limit=10):
    with open(file_name, mode="a", encoding="utf-8") as file:
        for _ in range(limit):
            file.write(validate_name().capitalize() + "\n")


fill_file()
