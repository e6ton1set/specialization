# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.

import logging
from datetime import datetime
import argparse

WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTH = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')

logging.basicConfig(filename='task_4.log', filemode='a', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='Get_date',
                                     description='Parser for function get_date',
                                     epilog='Используйте модуль для поиска даты из строки. '
                                            'Например: python task_5.py -d 2 -m ноябрь -w четверг')
    parser.add_argument('-d', '--day', default=1, help='Какой по счёту день недели')
    parser.add_argument('-w', '--weekday', default=datetime.now().weekday(), help='Название дня недели')
    parser.add_argument('-m', '--month', default=datetime.now().month, help='Название месяца')
    args = parser.parse_args()
    return get_date(f'{args.day} {args.weekday} {args.month}')


def get_date(date: str) -> datetime:
    try:
        amount, weekday, month = date.split()
    except ValueError:
        logger.error(f'Ваша строка "{date}" не может быть разделена\n'
                     f'Пример запроса: 2-ой четверг ноября')
        return None
    amount = int(amount[0])
    weekday = WEEKDAYS.index(weekday[:3])
    month = 1 + MONTH.index(month[:3])
    index = 0
    for day in range(1, 32):
        res_date = datetime(day=day, month=month, year=datetime.now().year)
        if res_date.weekday() == weekday:
            index += 1
            if index == amount:
                return res_date


if __name__ == '__main__':
    print(parse())