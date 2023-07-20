# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def print_sort_text(text: str):
    list_text = sorted(text.split())
    max_len_word = 0
    for word in list_text:
        if len(word) > max_len_word:
            max_len_word = len(word)

    for i, word in enumerate(list_text, start=1):
        print(f'{i}. {word:>{max_len_word}}')


text = input('Введите текст: \t')
print_sort_text(text)
