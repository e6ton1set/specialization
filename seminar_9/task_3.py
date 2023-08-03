# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable


def param_deco(amount_calls: int) -> Callable:
    result = []

    def deco(func: Callable) -> list:
        def wrapper(*args, **kwargs):
            for _ in range(amount_calls):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@param_deco(10)
def sum_nums(*args):
    return sum(args)


if __name__ == '__main__':
    print(sum_nums(22, 55, 77))
