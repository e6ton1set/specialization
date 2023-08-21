# Задание N4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину прямоугольника
# и встройте контроль недопустимых значений (отрицательных).
# 📌 Используйте декораторы свойств.

class Rectangle:
    """
    Rectangle class representation.
    """

    def __init__(self, a: float, b: float = None):
        """
        Takes rectangle sides. Adds then to class instance.
        If only one provided, a square assumed.
        """
        self.__a = a
        self.__b = b if b is not None else a

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value > 0:
            self.__a == value
        else:
            raise ValueError(f'Значение {self.__a} меньше 1')

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value > 0:
            self.__b == value
        else:
            raise ValueError(f'Значение {self.__b} меньше 1')

    def get_perimeter(self) -> float:
        """Returns perimeter (sum of all sides) of rectangle/square."""
        return 2 * (self.__a + self.__b)

    def get_area(self) -> float:
        """Returns area (product of two sides) of rectangle/square."""
        return self.__a * self.__b

    def __add__(self, other):
        """
        Allows to add one Rectangle instance to another by their perimeters.
        Returns new class instance with new sides.
        """
        sum_perimeter = self.get_perimeter() + other.get_perimeter()
        k = sum_perimeter / self.get_perimeter()
        return Rectangle(self.__a * k, self.__b * k)

    def __sub__(self, other):
        """
        Allows to subtract one Rectangle instance to another by their perimeters.
        Returns new class instance with new sides.
        """
        sub_perimeter = abs(self.get_perimeter() - other.get_perimeter())
        k = sub_perimeter / self.get_perimeter()
        return Rectangle(self.__a * k, self.__b * k)

    def __eq__(self, other):
        """Returns is Rectangle instance equal to another by its areas or not"""
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        """Returns is Rectangle instance area less than other's"""
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """Returns is Rectangle instance area less or equal than other's"""
        return self.get_area() <= other.get_area()

    def __repr__(self):
        return f'Rectangle({self.__a}, {self.__b})'

    def __str__(self):
        if self.__a == self.__b:
            return f'Square with side {self.__a}'
        else:
            return f'Rectangle with sides {self.__a} and {self.__b}'


if __name__ == '__main__':
    rect_1 = Rectangle(5, 10)
    rect_2 = Rectangle(10, 20)
    rect_1.b = 22
    print(rect_1.b)
