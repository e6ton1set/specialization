# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):
    pass


class LevelException(MyException):
    pass


class AccessException(MyException):
    pass
