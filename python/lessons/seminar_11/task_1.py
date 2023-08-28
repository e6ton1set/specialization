# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.


import time


class MyString(str):
    """
    If you use string, this class will also show you creator's name and time of an object
    """
    def __new__(cls, text: str, author: str):
        """
        Adding parameters to the parent class str
        :param text:
        :param author:
        """
        print('Start __new__')
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = round(time.time(), 2)

        return instance

    def __str__(self):
        """
        Show info to console
        :return:
        """
        return f'Text: {super().__str__()}\nCreated by {self.author} at {self.time}'


my_string_1 = MyString(author='Ruslan', text='Hello, my friend! How are you?')
# help(MyString)
print(MyString.__doc__)
