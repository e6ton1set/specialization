# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.


my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 22, 22, 44, 44, 55, 55, 55, 55, 55, 1, 2]
new_list = []

# for i in range(len(my_list)):
#     if my_list[i] % 2 != 0:
#         new_list.append(i + 1)
#
# print(new_list)

# ещё решение

for i, value in enumerate(my_list, start=1):
    if value % 2 != 0:
        new_list.append(i)

print(new_list)