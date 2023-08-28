# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def get_len(self) -> float:
        return round((pi * 2 * self.radius), 2)

    def get_square(self) -> float:
        return round((pi * (self.radius**2)), 2)


circle_1 = Circle(12)
print(circle_1.get_len())
print(circle_1.get_square())
