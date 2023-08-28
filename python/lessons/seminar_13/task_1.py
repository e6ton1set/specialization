# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

import logging

logging.basicConfig(filename='task_1.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def input_num():
    log_data = []
    while True:
        num_user = input('Введите целое (int) или вещественное (float) число:\t')
        try:
            res = float(num_user)
            log_data.append(num_user)
            logger.info(log_data)
            break
        except ValueError as e:
            print(f'Вы ввели {type(num_user)}, а нужно int или float.\n'
                  f'Повторите ввод!\n')
            log_data.append(num_user)
            logger.info(log_data)
    return res


if __name__ == '__main__':
    print(input_num())