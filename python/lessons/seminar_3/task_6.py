# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки

text = input('Введите текст: \t')
list_text = sorted(text.split())

max_len_world = 0
for world in list_text:
    if len(world) > max_len_world:
        max_len_world = len(world)

for i, world in enumerate(list_text, start=1):
    print(f'{i}. {world: >{max_len_world}}')
