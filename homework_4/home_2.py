# ✔Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def get_kwargs_dict(**kwargs: object) -> dict[str: str]:
    res = {}
    for key, value in kwargs.items():
        res[str(value)] = key

    return res


print(get_kwargs_dict(name=['Lex', 'App'], age=22.33))
