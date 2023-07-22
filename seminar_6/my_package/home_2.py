# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
# код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг
# друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
# бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
# 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если
# бьют - ложь.

"""queen
"""

__all__ = ['if_queen_beat']

field = 8
x = []
y = []


def if_queen_beat() -> bool:
    count = 0
    for i in range(field):
        new_x, new_y = [int(step) for step in input(f'Введите положение ' \
                                                    f'фигуры {i+1} через пробел:\n').split()]
        x.append(new_x)
        y.append(new_y)

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
    if_queen_beat()
