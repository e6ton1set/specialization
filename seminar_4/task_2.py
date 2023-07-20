# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def get_unicode_text(text: str) -> list[int]:
    uni_set = set(map(ord, text))
    convert_to_list = sorted(list(uni_set), reverse=True)
    return convert_to_list


input_text = input('Введите текст:\t')
print(get_unicode_text(input_text))