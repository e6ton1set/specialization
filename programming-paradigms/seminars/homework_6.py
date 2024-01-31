"""
Домашнее задание 6 по курсу "Парадигмы программирования и языки парадигм".

Контекст:
Предположим, что мы хотим найти элемент в массиве (получить его индекс).
Массив уже отсортирован. Нужно использовать алгоритм бинарного поиска:
сначала берём элемент находящийся посередине и сравниваем с тем, который мы хотим найти.
Если центральный э-т больше нашего, рассматриваем массив слева от центрального,
а если больше - справа, и повторяем до тех пор, пока не найдём наш э-т.

Задача:
Написать программу на любом языке в любой парадигме для бинарного поиска.
На вход подаётся целочисленный массив и число. На выходе - индекс элемента или -1,
если э-та нет в массиве.

Пояснение: императивный структурно-процедурный стиль.
"""

import array as arr


def binary_search(array: arr.array, target: int) -> int:
    if type(array) is not arr.array or type(target) is not int:
        raise TypeError("Array must be instance of arr.array('int'[])")

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = array[mid]
        if target == mid_val:
            return array.index(mid_val)
        if mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return KeyError('-1')


try:
    input_data = arr.array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
    print(f"Элемент найден, его индекс -> {binary_search(input_data, 110)}")
    print(type(binary_search(input_data, 110)))
    print(f"Элемент не найден {binary_search(input_data, -555)}")
    # print(f"Элемент найден, его индекс -> {binary_search(input_data, 'hi')}")
    print(f"Элемент найден, его индекс -> {binary_search([1, 2, 'hi'], -555)}")
except Exception as e:
    print(f"Error: {e}")