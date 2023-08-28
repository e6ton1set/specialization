# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях

input_text = input('Введите данные: \n')
res = None

if input_text.count('-') == 1 and input_text.replace('-', '').isdecimal():
    res = abs(int(input_text))
elif input_text.replace('.', '', 1).replace('-', '').isdecimal() and input_text.count('-') <= 1\
        and input_text[1:].count('-') == 0 and input_text.count('.') == 1:
    res = float(input_text)
elif not input_text.islower():
    res = input_text.lower()
else:
    res = input_text.upper()

print(res, type(res))