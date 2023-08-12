# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from random import randint
from task_3 import Human, Gender


class Worker(Human):
    MAX_LEVEL = 7
    MIN_ID = 100_000
    MAX_ID = 999_999

    def __init__(self, name: str, surname: str, patronymic: str,
                 age: int, profession, gender: Gender, id_worker: int):
        super().__init__(name, surname, patronymic,
                         age, profession, gender)
        if self.MIN_ID < id_worker <= self.MAX_ID:
            self.id_worker = id_worker
        else:
            self.id_worker = randint(self.MIN_ID, self.MAX_ID)

    def get_level(self) -> int:
        digit_of_id = sum((int(n) for n in str(self.id_worker)))
        return digit_of_id % self.MAX_LEVEL


worker_1 = Worker('Alise', 'Grace', 'Eivor', 33, 'Doctor', Gender.female, 777_777)
print(f'{worker_1.get_level() = }')