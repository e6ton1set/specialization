# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    """
    Одиночный класс для хранения данных о последнем экземляре
    """
    _instance = None

    def __init__(self, text: str, num: int | float | complex):
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """
        Метод, который сохраняет в list все значения экземляра до текущего (не включительно)
        :param args:
        :param kwargs:
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_nums = []
            cls._instance.archive_text = []
        else:
            cls._instance.archive_nums.append(cls._instance.num)
            cls._instance.archive_text.append(cls._instance.text)

        return cls._instance

    def __str__(self):
        """
        Method for displaying information to the user
        """
        return f'Text archive -> {self.archive_text}\n' \
               f'Nums archive -> {self.archive_nums}'

    def __repr__(self):
        """
        A method for displaying information to a colleague
        """
        return f'Текущее значение числа: {self.num}\nТекущее значение строки: {self.text}'


item_1 = Archive('text1', 55)
item_2 = Archive('text2', 254785.1054)
item_3 = Archive('text3', 0o11010010101)
item_3 = Archive('text3', 24343424)
# print(Archive._instance.archive_nums)
# print(Archive._instance.archive_text)
# print(Archive.__new__.__doc__)

# print(item_1)
print(repr(item_3))
