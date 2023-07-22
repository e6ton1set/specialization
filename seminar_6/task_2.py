# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных
# границах и пользователь должен угадать его за
# заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если
# попытки исчерпаны - ложь.

from random import randint as rnd

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
    data = input('Введите начало и конец диапозона через пробел\n')
    start, stop = map(int, data.split())
    print(get_random_num(start, stop))