# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату

import logging
from datetime import datetime

WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTH = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')

logging.basicConfig(filename='task_4.log', filemode='a', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


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
    print(get_date('понедельник января'))