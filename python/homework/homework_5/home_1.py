# Напишите функцию, которая принимает на вход строку —
# - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

path: str = '/learning_python/homework_assignments/homework_5/home_1.py'


def get_path_tuple(link: str) -> tuple:
    *route, file = link.split('\\')
    route = '\\'.join(path)
    name, exp = file.split('.')
    res_tuple = (route, name, exp)
    return res_tuple


print(get_path_tuple(path))
print(type(get_path_tuple(path)))
