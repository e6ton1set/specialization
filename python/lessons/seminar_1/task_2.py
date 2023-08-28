# Напишите программу, которая запрашивает год
# и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif.
# Откажитесь от магических чисел.
# Обязательно учтите год ввода Григорианского календаря.
# В коде должны быть один input и один print.


year = int(input('Введите год для проверки на високосность: '))
GREGORIAN = 1582
MULTI_400 = 400
MULTI_100 = 100
MULTI_4 = 4

leap_year = '{} високосный'
non_leap_year = '{} не високосный'
not_gregorian = '{} не входит в диапозон Григорианского календаря'
result = ''

if year <= GREGORIAN:
    result = not_gregorian.format(year)
elif (year % MULTI_4 == 0 and year % MULTI_100 != 0) or year % MULTI_400 == 0:
    result = leap_year.format(year)
else:
    result = non_leap_year.format(year)

print(result)

