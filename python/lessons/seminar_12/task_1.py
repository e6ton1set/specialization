# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


import json
from collections import deque


class Factorial:
    def __init__(self, k):
        self._history = deque(maxlen=k)

    def __call__(self, number: int):
        mult = 1
        for i in range(2, number + 1):
            mult *= i
        self._history.append({number: mult})
        return mult

    def show_history(self):
        return self._history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = {}
        while self._history:
            data.update(self._history.popleft())
        with open('history_operation.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)


if __name__ == '__main__':
    test_factorial = Factorial(2)
    with test_factorial as f:
        test_factorial(22)
        test_factorial(6)
        print(test_factorial.show_history())
