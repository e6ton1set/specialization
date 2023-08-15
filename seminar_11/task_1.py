# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class MyString(str):
    def __new__(cls, text: str, author: str):
        print('Start __new__')
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = round(time.time(), 2)

        return instance

    def __str__(self):
        return f'Text: {super().__str__()}\nCreated by {self.author} at {self.time}'


my_string_1 = MyString(author='Ruslan', text='Hello, my friend! How are you?')
print(my_string_1)