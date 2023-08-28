# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

def calc_factorial(number: int):
    mult = 1
    for item in range(2, number + 1):
        mult *= item
    return mult


class FactorialRange:
    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            cur_fact = calc_factorial(self.start)
            self.start += self.step
            return cur_fact
        raise StopIteration


if __name__ == '__main__':
    fact_range = FactorialRange(11, 2)
    for i, res in enumerate(fact_range, 10):
        print(i, res)

