# Задание №6
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.

import asyncio
import os

PATH = 'parser_url'
count = 0


async def get_amount_worlds(file_path) -> None:
    global count
    with open(file_path, encoding='utf-8') as f:
        count = len(f.read().split())
    print(f"Значение счетчика: {count :_}")


async def main():
    tasks = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            tasks.append(asyncio.create_task(get_amount_worlds(file_path)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print(f'Финальное значение счётчика: {count}')


