# Задание №3
# � Улучшаем задачу 2
# � Добавьте возможность запуска функции “угадайки”
# из модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов:
# параметры вызова функции.
# � Для преобразования строковых аргументов
# командной строки в числовые параметры
# используйте генераторное выражение.

from random import randint as rnd
from sys import argv

"""Угадай число
"""

START = 0
STOP = 100
AMOUNT = 2


def get_random_num(start: int, end: int, amount=AMOUNT) -> bool:
    flag = False
    num = rnd(start, end)
    while amount > 0:
        num_user = int(input('Введите число:\t'))
        if num_user == num:
            print('Вы угадали!\t')
            flag = True
        elif num_user < num:
            print('Больше')
            amount -= 1
        else:
            print('Меньше')
            amount -= 1

    return flag


if __name__ == '__main__':  #не будет выполняться при импорте модуля
    name, *param = argv
    print(get_random_num(*(int(elem) for elem in param)))