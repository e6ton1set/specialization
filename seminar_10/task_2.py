# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length: int, width: int = None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def get_perimeter(self) -> int:
        return 2 * (self.length + self.width)

    def get_square(self) -> int:
        return self.length * self.width


rect_1 = Rectangle(1, 2)
rect_2 = Rectangle(5)
print(f'{rect_1.get_perimeter() = }'
      f'\n{rect_1.get_square() = }')
print(f'{rect_2.get_perimeter() = }'
      f'\n{rect_2.get_square() = }')
