# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data_list = [1, 1, 2, 3, 4, 4, 20, 20, 55, 55, 55, 55,
             'Привет', 'Привет', 'Привует', (2, 12), (2, 12)]
res_list = []

for item in data_list:
    if data_list.count(item) >= 2:
        if item not in res_list:
            res_list.append(item)

print(res_list)