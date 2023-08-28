# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


TEN = 10
HUNDRED = 100
THOUSAND = 1000
ZERO = 0

result = ''
if_ten = 'Вы ввели цифру число {}\nЕё квадрат равен {}'
if_hundred = 'Вы ввели двухзначное число {}\nПроизведение цифр в нём равно {}'
if_thousand = 'Вы ввели трехзначное число {}\nОбратный порядок цифр в нём {}'

num = int(input('Введите целое число от 1 до 999 включительно: \n'))
while ZERO < num < THOUSAND:
    if num < TEN:
        sqrt_num = num ** 2
        result = if_ten.format(num, sqrt_num)
        break
    elif num < HUNDRED:
        temp_num = num
        while num != ZERO:
            first_digit = num % TEN
            last_digit = num // TEN
            mult_digits = first_digit * last_digit
            result = if_hundred.format(temp_num, mult_digits)
            num //= HUNDRED
        break
    else:
        temp_num = num
        temp_num = str(temp_num)
        temp_num = temp_num[::-1]
        result = if_thousand.format(num, temp_num)
        break
else:
    print('Число не из диапозона от 1 до 999 включительно')

print(result)
