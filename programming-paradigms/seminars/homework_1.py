"""
Домашнее задание 1 по курсу "Парадигмы программирования и языки парадигм".
Задание:
Дан список целых чисел numbers.
Необходимо написать в императивном стиле процедуру для сортировки числа в списке в порядке убывания.
Можно использовать любой алгоритм сортировки.
"""


# Декларативный стиль
def sort_list_declarative(numbers: list[int]) -> list[int]:
    curr_list = numbers.copy()
    curr_list.sort(reverse=True)
    return curr_list


# Императивный стиль
def sort_list_imperative(numbers: list[int]) -> list[int]:
    curr_list = numbers.copy()
    n = len(curr_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if curr_list[j] < curr_list[j+1]:
                curr_list[j], curr_list[j+1] = curr_list[j+1], curr_list[j]
    return curr_list


if __name__ == '__main__':
    numbers_list = [x for x in range(-20, 21)]
    print(f"Declarative -> {sort_list_declarative(numbers_list)}")
    print(f"Imperative -> {sort_list_imperative(numbers_list)}")
