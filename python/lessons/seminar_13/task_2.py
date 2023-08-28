# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений


def my_get(dictonary: dict, key: str, default: int | float = None) -> int | float | None:
    res = default
    try:
        res = dictonary[key]
    except KeyError as ke:
        print(f'Произошла ошибка ключа: {ke}')
    return res


if __name__ == '__main__':
    my_dict = {'a': 1, 'b': 2.2}
    print(my_get(my_dict, 'b', 0))