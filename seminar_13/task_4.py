# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

from exception_task_3 import LevelException, AccessException
import json
from typing import Set


class User:
    def __init__(self, name: str, user_id: int, user_level: int):
        self.name = name
        self.user_id = user_id
        self.user_level = user_level

    def __str__(self):
        return f'{self.name}, id: {self.user_id}, level: {self.user_level}'


def load_users_json(json_file_path: str) -> Set[User]:
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    users = set()

    for user in data:
        users.add(User(user['name'], int(user['user_id']), int(user['access_level'])))
    return users


if __name__ == '__main__':
    print(*load_users_json('users.json'), sep='\n')


