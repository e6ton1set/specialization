# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Fish:
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        self.name = name
        self.color = color
        self.size = size
        self.max_depth = max_depth

    def show_info(self):
        print(f'Максимальная глубина: {self.max_depth}')


class Bird:
    def __init__(self, name: str, color: str, size: float, max_height: float):
        self.name = name
        self.color = color
        self.size = size
        self.max_height = max_height

    def show_info(self):
        print(f'Максимальная высота: {self.max_height}')


class Cat:
    def __init__(self, name: str, color: str, size: float, breed: str):
        self.name = name
        self.color = color
        self.size = size
        self.breed = breed

    def show_info(self):
        print(f'Порода: {self.breed}')


if __name__ == '__main__':
    fish_1 = Fish('Fish', 'Yellow', 3.3, 100)
    bird_1 = Bird('Bird', 'Red', 22.5, 500)
    cat_1 = Cat('Cat', 'Blue', 10.2, 'Myu')
    fish_1.show_info()
    bird_1.show_info()
    cat_1.show_info()
