# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
# код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг
# друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
# бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
# 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если
# бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.

from random import randint

"""queen
"""

field = 8

__all__ = ['if_queen_beat', 'spread_queen']


def spread_queen() -> list[int]:
    x = []
    for _ in range(1, field + 1):
        x.append(randint(1, field + 1))
    return x


def if_queen_beat(x: list[int], y: list[int]) -> bool:
    correct = True
    for i in range(field):
        for j in range(i + 1, field):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

    if correct:
        print(correct)
    else:
        print(correct)


if __name__ == '__main__':
    x = spread_queen()
    y = spread_queen()
    print(if_queen_beat(x, y))
