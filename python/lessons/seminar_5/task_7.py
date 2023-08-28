# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

START = 2


def get_prime_nums(num: int):
    temp: int = 2

    while 1 < temp <= num:
        is_prime = True
        for elem in range(START, temp//2+1):
            if temp % elem == 0:
                temp += 1
                is_prime = False
                break
        if is_prime:
            yield temp
            temp += 1


for n in (get_prime_nums(30)):
    print(n, end=' ')
    print(type(n))
