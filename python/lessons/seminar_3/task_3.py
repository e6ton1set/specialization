# Задание №3
# ✔ Создайте вручную кортеж, содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

some_tuple = (2, 6.6, 'Hello', -44, True, None, 'Привет', 33.22)
res_dict = {}

# for item in some_tuple:
#     if type(item) in res_dict.keys():
#         res_dict[type(item)].append(item)
#     else:
#         res_dict[type(item)] = [item]
#
# print(res_dict)

# чтобы каждый раз не писать код выше, есть втроенные методы в словорях

for item in some_tuple:
    key = res_dict.setdefault(type(item), list())
    key.append(item)

print(res_dict)