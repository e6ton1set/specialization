# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

START = 1
STOP = 100

for i in range(START, STOP):
    message = None
    if i % 15 == 0:
        message = 'FizzBuzz'
    elif i % 3 == 0:
        message = 'Fizz'
    elif i % 5 == 0:
        message = 'Buzz'
    else:
        message = i
    print(message)

# *вариант с генератором

task_5_gen = ('FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n for n in
              range(1, 101))
print(*task_5_gen, sep='\nGEN -> ')
