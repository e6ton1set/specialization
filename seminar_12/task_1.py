# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

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


if __name__ == '__main__':
    test_factorial = Factorial(2)
    test_factorial(11)
    test_factorial(2)
    print(test_factorial.show_history())
