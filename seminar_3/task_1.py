# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def sort_print_text(text: str):
    input_list = sorted(text.split())
    max_len = 0
    for word in input_list:
        if len(word) > max_len:
            max_len = len(word)

    for num, word in enumerate(input_list, start=1):
        print(f'{num}. {word:>{max_len}}')


input_text = input('Введите текст: ')
sort_print_text(input_text)

