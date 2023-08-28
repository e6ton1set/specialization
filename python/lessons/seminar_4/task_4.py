# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# list_nums = [10, 20, 33, 5, 66, 107, 44]


# def bubble_sort(nums_list: int) -> list[int]:
#     for i in range(len(nums_list) - 1):
#         for j in range(i + 1, len(nums_list)):
#             if nums_list[j] < nums_list[i]:
#                 nums_list[j], nums_list[i] = nums_list[i], nums_list[j]
#
#     return nums_list
#
#
# print(bubble_sort(list_nums))
# in place - на месте
# если у функции есть окончание 'ed' (например, sorted) -> возвращает изменённую копию объекта
# если нет, то функция мутирует текущий объект


# ЗАДАЧА с собеса

print([0] * 2)
print('___________')
print([[0] * 2] * 2)
print('___________')
x = [[0] * 2] * 2
x[0][0] = 4
print(x)
