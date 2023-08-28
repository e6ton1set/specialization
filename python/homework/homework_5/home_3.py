# Создайте функцию генератор чисел Фибоначчи

def get_fibonacci(num: int) -> list[int]:
    fib_list = [0, 1, 1]
    fib1 = 1
    fib2 = 1
    if num == 0 or num == 1:
        return 1
    for i in range(2, num+1):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib2)

    return fib_list


user_num = int(input('Введите число, для которого хотите найти последовательность'
                     'чисел Фибоначчи:\t'))
print(f'Результат:\n{get_fibonacci(user_num)}')