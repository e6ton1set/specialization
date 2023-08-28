# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from python.lessons.seminar_10 import task_5
from enum import Enum


class EnumerationAnimals(Enum):
    fish = task_5.Fish
    bird = task_5.Bird
    cat = task_5.Cat


class Factory:
    def __init__(self):
        self.animals = []

    def create_animal(self, animal_class: EnumerationAnimals, name: str, color: str, size: float, *args, **kwargs) \
            -> task_5.Animal:
        instance_animal = animal_class.value(name, color, size, *args, **kwargs)
        self.animals.append({'Тип': animal_class.name, 'Животное': instance_animal})
        return instance_animal

    def show_animals(self):
        for i, animal in enumerate(self.animals):
            print(i + 1, animal)


if __name__ == '__main__':
    factory = Factory()
    cat_1 = factory.create_animal(EnumerationAnimals.cat, 'Cat', 'Blue', 4.2, 'Myu')
    bird_1 = factory.create_animal(EnumerationAnimals.bird, 'Bird', 'Green', 9.4, 150)
    factory.show_animals()
