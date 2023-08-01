# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json


def json_to_csv(json_file_path: str, csv_file_path: str) -> None:

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    rows = []

    for access_level, users in data.items():
        for user_id, name in users.items():
            rows.append({'access_level': int(access_level), 'users_id': int(user_id), 'name': name})

    with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
        csv_dict = csv.DictWriter(csv_file, fieldnames=['access_level', 'users_id', 'name'], dialect='excel-tab')
        csv_dict.writeheader()
        csv_dict.writerows(rows)


json_to_csv('task_2.json', 'task_3.csv')

