# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os


def request_data_and_write_to_json(json_file):
    users_id = set()
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as temp_json:
            data = json.load(json_file)
            for user in data.values():
                users_id.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}

    while True:
        name = input('Введите имя:\t')
        if not name:
            break
        id_user = input('Введите ID:\t')
        access_level = input('Введите уровень доступа:\t')

        if id_user in users_id:
            continue
        data[access_level][id_user] = name

        with open(json_file, 'w', encoding='utf-8') as res_json:
            json.dump(data, res_json, ensure_ascii=False, indent=2)


request_data_and_write_to_json('task_2.json')
