# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def convert_to_json(path_file: str, path_json: str) -> None:
    res_dict = {}
    with open(path_file, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            name, num = line.split('\t')
            res_dict[name.capitalize()] = float(num)

    with open(path_json, 'w', encoding='utf-8') as output_file:
        json.dump(res_dict, output_file, ensure_ascii=False, indent=2)


convert_to_json('task_1.txt', 'task_1.json')