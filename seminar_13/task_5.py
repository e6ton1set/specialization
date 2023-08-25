# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json
from typing import Set
from exception_task_3 import LevelException, AccessException
from task_4 import User


class Project:
    def __init__(self, json_file_path: str):
        self.admin = None
        self.json_file_path = json_file_path
        self.users = self.load_users_json()

    def load_users_json(self) -> Set[User]:
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        users = set()

        for user in data:
            users.add(User(user['name'], int(user['user_id']), int(user['access_level'])))
        return users

    def entrance(self, name: str, user_id: int):
        test_user = User(name, user_id, 0)
        if test_user in self.users:
            for user in self.users:
                if user == test_user:
                    self.admin = user
        else:
            raise AccessException

    def add_user(self, name: str, user_id: int, user_level: int):
        if user_level > self.admin.user_level:
            raise LevelException
        new_user = User(name, user_id, user_level)
        self.users.add(new_user)
        self.save_users()

    def save_users(self):
        with open(self.json_file_path, 'w', encoding='utf-8') as json_file:
            data = [{'name': user.name, 'user_id': user.user_id, 'access_level': user.user_level}
                    for user in self.users]
            json.dump(data, json_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    proj_1 = Project('users.json')
    proj_1.entrance('Анастасия', 143)
    proj_1.add_user('Геша', 150, 1)
    proj_1.add_user('Ольга', 151, 1)
    print(*proj_1.users, sep='\n')
