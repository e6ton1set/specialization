# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

from functools import wraps
from typing import Callable
import json
from os.path import exists


def save_param_and_result_func_to_json(func: Callable) -> Callable[[list, dict], int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = f'{func.__name__}.json'
        data = []

        if exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

        result = func(*args, **kwargs)
        curr_data = {
            'args': args,
            **kwargs,
            'result': result
        }

        data.append(curr_data)
        with open(file_path, 'w', encoding='utf-8') as add2json:
            json.dump(data, add2json, indent=2, ensure_ascii=False)

        return result

    return wrapper


@save_param_and_result_func_to_json
def sum_num(*args, **kwargs) -> int:
    return sum(args)


@save_param_and_result_func_to_json
def concat_str(*args, **kwargs) -> int:
    return ''.join(args)


if __name__ == '__main__':
    # sum_num(10, 20, 30, a=-2.22)
    concat_str('100', '200', '300', hey='hello')