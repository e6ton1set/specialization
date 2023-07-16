# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды

from collections import defaultdict

# DUBLICATES = 2
#
# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 22, 22, 44, 44, 55, 55, 55, 55, 55, 1, 2]
# res_dict = {}
#
# for item in my_list:
#     value = res_dict.setdefault(item, 0)
#     res_dict[item] += 1
#
# for key, value in res_dict.items():
#     if value == DUBLICATES:
#         for _ in range(DUBLICATES):
#             my_list.remove(key)
#
# print(res_dict)
# print(my_list)

# решение с использованием библиотеки collections

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 22, 22, 44, 44, 55, 55, 55, 55, 55, 1, 2]
res_dict = defaultdict(int)

for item in my_list:
    res_dict[item] += 1

print(res_dict)