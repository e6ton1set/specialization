# Погружение в Python
# Задание №6
# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# � Функция формирует словарь с информацией о
# результатах отгадывания.
# � Для хранения используйте защищённый словарь
# уровня модуля.
# � Отдельно напишите функцию, которая выводит
# результаты угадывания из защищённого словаря в
# удобном для чтения виде.
# � Для формирования результатов используйте
# генераторное выражение.

_data = {}


def puzzle(puzzle_text: str, answers: list[str], trials: int):
    print(puzzle_text)

    try_count = 1
    while trials > 0:
        current_try = input(f'Осталось попыток: {trials}\n-> Ваш ответ: ')
        if current_try in answers:
            return try_count
        try_count += 1
        trials -= 1
    else:
        return trials


def get_storage(trial_amount: int = 3):
    puzzle_dict = {'Загадка 1': ['да', 'наверное'],
                   'Загадка 2': ['да', 'вряд ли'],
                   'Загадка 3': ['да', 'нет же!'],
                   }
    for puzzle_text, answer_text in puzzle_dict.items():
        res = puzzle(puzzle_text, answer_text, trial_amount)
        save_stat(puzzle_text, res)


def save_stat(puzzle_text: str, try_count: int):
    _data.update({puzzle_text: try_count})


def show_stat():
    print('_______________________________________\nСТАТИСТИКА\n_______________________________________')
    output = '\n'.join((f'Загадка {puzzle_text} '
                        f'{f"угадана с {trial_amount} попытки" if trial_amount > 0 else "не угадана"}'
                        for puzzle_text, trial_amount in _data.items()))
    print(output)


if __name__ == '__main__':
    get_storage()
    show_stat()
