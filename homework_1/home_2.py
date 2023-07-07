# Выведите в консоль таблицу умножения от 2х2 до 9х10
# как на школьной тетрадке.

START = 1
END = 10

for i in range(START, END):
    for j in range(START, END + 1):
        print(f'{i} x {j} = {i * j}')
    print(' ')
