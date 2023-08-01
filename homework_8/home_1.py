# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

__all__ = ['bypass_dirs_save_to_csv_pickle']


def bypass_dirs_save_to_csv_pickle(dir_path: str) -> None:
    dict_json = {}

    for path, file, name in os.walk(dir_path):
        dict_json[f'Directory - {dir_path}'] = [
            f'File - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in name]

    with open('home_1.json', 'w', encoding='utf-8') as json_file:
        json.dump(dict_json, json_file, indent=2, ensure_ascii=False)

    data = [["Dir", "Files"]]

    for key, value in dict_json.items():
        data.append([key, value])

    with open('home_1.csv', 'w', encoding='utf-8') as csv_file:
        write_csv = csv.writer(csv_file, dialect='excel-tab')
        write_csv.writerows(data)

    with open('home_1.pickle', 'wb') as pickle_file:
        pickle.dump(dict_json, pickle_file)


bypass_dirs_save_to_csv_pickle('.')
