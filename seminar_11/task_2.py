# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    _instance = None

    def __init__(self, text: str, num: int | float | complex):
        print('Start __init__')
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        print('Start __new__')

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_nums = []
            cls._instance.archive_text = []
        else:
            cls._instance.archive_nums.append(cls._instance.num)
            cls._instance.archive_text.append(cls._instance.text)

        return cls._instance


item_1 = Archive('text1', 55)
item_2 = Archive('text2', 254785.1054)
item_3 = Archive('text3', 0o11010010101)
item_3 = Archive('text3', 24343424)
print(Archive._instance.archive_nums)
print(Archive._instance.archive_text)
