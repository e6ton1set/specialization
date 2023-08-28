# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

input_text = input('Введите текст: ')
qty_dict = {}
new_dict = {}

for char in set(input_text):
    qty_dict[char] = input_text.count(char)

for char in input_text:
    new_dict.setdefault(char, 0)
    new_dict[char] += 1

print(qty_dict)
print(new_dict)