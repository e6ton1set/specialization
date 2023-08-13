# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name: str, color: str, size: float):
        self.name = name
        self.color = color
        self.size = size

    def show_unique(self):
        pass


class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        super().__init__(name, color, size)
        self.max_depth = max_depth

    def show_unique(self):
        print(f'Максимальная глубина: {self.max_depth}')


class Bird(Animal):
    def __init__(self, name: str, color: str, size: float, max_height: float):
        super().__init__(name, color, size)
        self.max_height = max_height

    def show_unique(self):
        print(f'Максимальная высота: {self.max_height}')


class Cat(Animal):
    def __init__(self, name: str, color: str, size: float, breed: float):
        super().__init__(name, color, size)
        self.breed = breed

    def show_unique(self):
        print(f'Порода: {self.breed}')


if __name__ == '__main__':
    fish_1 = Fish('Fish', 'Yellow', 3.3, 100)
    bird_1 = Bird('Bird', 'Red', 22.5, 500)
    cat_1 = Cat('Cat', 'Blue', 10.2, 'Myu')

    animals = (fish_1, bird_1, cat_1)

    for animal in animals:
        animal.show_unique()
