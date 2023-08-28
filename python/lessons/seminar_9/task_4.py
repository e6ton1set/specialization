# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from task_1 import decorator as validate
from task_2 import save_param_and_result_func_to_json as save_history
from task_3 import param_deco as trials


@trials(2)
@validate
@save_history
def guessing_num(steps: int, gues_num: int):
    for i in range(1, steps + 1):
        print(f'Текущая попытка: {i}')
        current_num = int(input('Попробуйте угадать число:\t'))
        if gues_num == current_num:
            print('Вы угадали!')
            break
        elif gues_num < current_num:
            print(f'Ваше число {current_num} больше |> загаданного ')
        else:
            print(f'Ваше число {current_num} меньше <| загаданного ')


if __name__ == '__main__':
    guessing_num(15, 3)