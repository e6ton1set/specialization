# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

import threading
import os

PATH = 'test'
count = 0


def get_amount_worlds(file_name: str) -> None:
    global count
    with open(file_name, encoding='utf-8') as f:
        count += len(f.read().split())


threads = []


def threads_count(directory):
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            t = threading.Thread(target=get_amount_worlds, args=(file_path,))
            threads.append(t)
            t.start()
            print(f'Сейчас значение счётчика: {count}')


if __name__ == '__main__':
    threads_count(PATH)

    for thread in threads:
        thread.join()

    for thread in threads:
        print(thread.is_alive())

