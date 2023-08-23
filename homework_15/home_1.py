# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" "Зачет"
# ставится, если Слушатель успешно выполнил задание.
# "Незачет" ставится, если Слушатель не выполнил задание.
# Критерии оценивания: 1 - Слушатель написал корректный код для задачи,
# добавил к ним логирование ошибок и полезной информаци

import logging
from typing import Callable
import argparse

logging.basicConfig(filename='home_1.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='get_fibonacci',
                                     description='выводит числа Фибоначчи',
                                     epilog='Используйте модуль для получения числовой последовательности '
                                            'Фибонначи до вашего числа. '
                                            'Пример запуска: python home_1.py -d 2 -m ноябрь -w четверг')
    parser.add_argument('-n', '--number', default=1, help='Граница расчёта чесел Фибонначи')
    args = parser.parse_args()
    return get_fibonacci(f'{args.number}')


def add2log(func: Callable):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        log_data = {"args": args, **kwargs, "result": res}
        logger.info(log_data)
        return res
    return wrapper


@add2log
def get_fibonacci(num: str) -> list[int]:
    num = int(num)
    fib_list = [0, 1, 1]
    fib1 = 1
    fib2 = 1
    ONE = 1
    if num == 0 or num == 1:
        return ONE
    for i in range(2, num+1):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib2)
    return fib_list


if __name__ == '__main__':
    print(parse())