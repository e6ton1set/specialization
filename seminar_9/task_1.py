# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток

from typing import Callable


def guess_number(steps: int, gues_num: int) -> Callable[[], None]:
    def guessing_num():
        for i in range(1, steps+1):
            print(f'Текущая попытка: {i}')
            current_num = int(input('Попробуйте угадать число:\t'))
            if gues_num == current_num:
                print('Вы угадали!')
                break
            elif gues_num < current_num:
                print(f'Ваше число {current_num} больше |> загаданного ')
            else:
                print(f'Ваше число {current_num} меньше <| загаданного ')
    return guessing_num


if __name__ == '__main__':
    game = guess_number(15, 3)  # переменная game хранит внутреннюю функцию guessing_num
    game()