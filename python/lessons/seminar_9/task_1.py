# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток

# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

# def guess_number(steps: int, gues_num: int) -> Callable[[], None]:
#     def guessing_num():
#         for i in range(1, steps+1):
#             print(f'Текущая попытка: {i}')
#             current_num = int(input('Попробуйте угадать число:\t'))
#             if gues_num == current_num:
#                 print('Вы угадали!')
#                 break
#             elif gues_num < current_num:
#                 print(f'Ваше число {current_num} больше |> загаданного ')
#             else:
#                 print(f'Ваше число {current_num} меньше <| загаданного ')
#     return guessing_num

from typing import Callable
import random
from functools import wraps


def decorator(func: Callable) -> Callable[[int, int], None]:
    min_number = 1
    max_number = 100
    min_steps = 1
    max_steps = 10

    @wraps(func)
    def wrapper(steps: int, gues_num: int, *args, **kwargs):
        if not min_number <= gues_num <= max_number:
            gues_num = random.randint(min_number, max_number)
        if not min_steps <= steps <= max_steps:
            steps = random.randint(min_steps, max_steps)

        return func(steps, gues_num, *args, **kwargs)

    return wrapper


@decorator
def guessing_num(steps: int, gues_num: int):
    for i in range(1, steps + 1):
        print(f'Текущая попытка: {i}')
        current_num = int(input('Попробуйте угадать число:\t'))
        if gues_num == current_num:
            print('Вы угадали!')
            break
        elif gues_num < current_num:
            print(f'Ваше число {current_num} больше |> загаданного ')
        else:
            print(f'Ваше число {current_num} меньше <| загаданного ')


if __name__ == '__main__':
    guessing_num(15, 4)
