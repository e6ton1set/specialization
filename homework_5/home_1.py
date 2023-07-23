# Напишите функцию, которая принимает на вход строку —
# - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

path: str = 'C:\\Users\\User\\PycharmProjects\\specialization\\homework_5\\home_1.py'


def get_path(link: str) -> tuple:
    *route, file = link.split('\\')
    route = '\\'.join(path)
    name, exp = file.split('.')
    res_tuple = (route, name, exp)
    return res_tuple


print(get_path(path))
print(type(get_path(path)))
