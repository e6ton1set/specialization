# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


import logging
from typing import Callable

FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(filename='task_3.log', encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')
loger = logging.getLogger(__name__)


def add2log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_dict = {'args': args, **kwargs}
        log_msg = f'{func.__name__}: {log_dict}. result: {result}'
        loger.info(log_msg)
        return result
    return wrapper


@add2log
def division(a: int, b: int) -> float:
    result = None
    try:
        result = a / b
    except ZeroDivisionError as e:
        result = float('inf')
    return result


if __name__ == '__main__':
    print(division(10, 2))
    print(division(10, 0))