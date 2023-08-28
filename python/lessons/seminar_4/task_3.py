# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def get_dict_unicode_chars(nums: str) -> dict[str: int]:
    num1, num2 = map(int, nums.split())
    dict_unicode_chars = {}

    for i in range(min(num1, num2), max(num1, num2) + 1):
        dict_unicode_chars[chr(i)] = i

    return dict_unicode_chars


two_nums = input('Введите два числа через пробел:\t')
print(get_dict_unicode_chars(two_nums))


