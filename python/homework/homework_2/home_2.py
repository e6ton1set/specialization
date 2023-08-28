# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

num1 = input('Введите первую дробь через /\n')
num2 = input('Введите первую дробь через /\n')
operation = input('Выберите операцию: "+" или "*"\n')


def get_sum_fractions(number1: str, number2: str, action: str) -> int:
    numerator1, denominator1 = number1.split('/')
    numerator2, denominator2 = number2.split('/')
    n1, d1 = int(numerator1), int(denominator1)
    n2, d2 = int(numerator2), int(denominator2)
    res = ''

    if (d1 or d2) == 0:
        res = 'Дробь не имеет значения, т.к. один из наменателей равен нулю.'
    elif '+' in action:
        res = n1 / d1 + n2 / d2
    elif '*' in action:
        res = n1 / d1 * n2 / d2

    return res


call = get_sum_fractions(num1, num2, operation)
print(f'Десятичные результат {operation}-ия дробей {num1} и {num2} равен {round(call, 2)}')

