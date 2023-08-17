# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from seminar_10.task_2 import Rectangle


class RectanglePro(Rectangle):
    """
    The class extends the capabilities of the Triangle class (from seminar_10.task_2) :
    difference, addition and comparison
    """

    def __add__(self, other):
        """
        Addition method
        """
        sum_perimeter = self.get_perimeter() + other.get_perimeter()
        side_a = self.length + other.length
        side_b = sum_perimeter / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __sub__(self, other):
        """
        Subtraction method
        """
        if self.get_perimeter() < other.get_perimeter():
            self, other = other, self
        diff = self.get_perimeter() - other.get_perimeter()
        side_a = abs(self.length - other.length)
        side_b = diff / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __eq__(self, other):
        """
        Equality check
        """
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """
        Checking for more
        """
        return self.get_square() > other.get_square()

    def __le__(self, other):
        """
        Checking for greater than or equal to
        """
        return self.get_square() >= other.get_square()

    def __str__(self):
        """
        Method for displaying information to the user
        """
        return f'P obj -> {self.get_perimeter()}\n' \
               f'S obj -> {self.get_square()} '


rect_1 = RectanglePro(2, 3)
rect_2 = RectanglePro(5, 6)
# print(rect_1.get_perimeter())
# print(rect_2.get_perimeter())
# rect_sum = rect_1 + rect_2
# rect_sub = rect_1 - rect_2
# print(rect_sum.get_perimeter())
# print(rect_sub.get_perimeter())
# print(rect_sum.width, rect_sum.length)
# print(rect_sub.width, rect_sub.length)
# print(rect_1.get_square(), rect_2.get_square())
# print(rect_1 != rect_2)
# print(RectanglePro.__doc__)
print(rect_1)