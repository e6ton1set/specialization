# ✔В модуль с проверкой даты добавьте возможность запуска в терминале с передачей
# даты на проверку.

from seminar_6.my_package.task_7 import check_date
from sys import argv

if __name__ == '__main__':
    name, date = argv
    print(check_date(date))