# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'


class Human:
    def __init__(self, name: str, surname: str, patronymic: str,
                 age: int, profession: str, gender: Gender):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._age = age
        self.profession = profession
        self.gender = gender

    def birthday(self):
        self._age += 1

    def get_age(self) -> int:
        return self._age

    def show_full_name(self) -> str:
        return f'Имя:\t{self.name:>14}\nФамилия:\t{self.surname:>10}' \
               f'\nОтчество:\t{self.patronymic:>10}'


if __name__ == '__main__':
    human_1 = Human('Alise', '---', 'Eivor', 33, 'Doctor', Gender.female)
    print(f'{human_1.get_age() = }')
    human_1.birthday()
    print(f'{human_1.get_age() = }')
    print(human_1.show_full_name())
    print('======================================================')
    human_2 = Human('Bob', '---', 'Jake', 28, 'Police', Gender.female)
    print(f'{human_2.get_age() = }')
    human_2.birthday()
    human_2.birthday()
    print(f'{human_2.get_age() = }')
    print(human_2.show_full_name())

