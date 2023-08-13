# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

import json


class Converter:
    def __init__(self, path_file: str, path_json: str):
        self.path_file = path_file
        self.path_json = path_json

    def convert_to_json(self) -> None:
        res_dict = {}
        with open(self.path_file, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                name, num = line.split('\t')
                res_dict[name.capitalize()] = float(num)

        with open(self.path_json, 'w', encoding='utf-8') as output_file:
            json.dump(res_dict, output_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    file_1 = Converter('text.txt', 'text.json')
    file_1.convert_to_json()
