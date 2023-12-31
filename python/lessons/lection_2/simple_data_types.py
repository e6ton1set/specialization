# БЛОКИ:
# ✔ простые типы данных и коллекции;
# ✔ аннотация типов;
# ✔ объект - его атрибуты и методы;
# ✔ простые объекты;
# ✔ математика в Python.

# ПРОСТЫЕ ТИПЫ ДАННЫХ
a = 5
a = 'hello world!'
a = 42.0 * 3.141592 / 2.71828
# Мы видим, что переменная a три раза принимает значения разных типов.
# Ошибок не возникло, т.к. у Python динамическая типизация, т.е.
# каждый раз переменная просто являлась указателем на объект

a = 5
print(type(a))
a = 'hello world!'
print(type(a))
a = 42.0 * 3.141592 / 2.71828
print(type(a))
print('___________________________')
# В первом случае переменная а указывает на объект целого типа int.
# Во втором случае переменная а указывает на объект типа строки str.
# В третьем случае переменная а указывает на объект типа с плавающей запятой float.

a = 5
print(type(a), id(a))
a = 'hello world!'
print(type(a), id(a))
a = 42.0 * 3.141592 / 2.71828
print(type(a), id(a))
print('___________________________')
# Таким образом, переменная а не перезаписывает своё значение,
# вместо этого она каждый раз указывает на другое место в памяти (новая коробка на складе).
# Т.е. типизация статическая, динамически меняется указатель на тот или иной объект.

data = 40
print(isinstance(data, int))
data = True
print(isinstance(data, int))
data = 3.14
print(isinstance(data, (float, complex, int)))
print('___________________________')
# Во втором случае True является подклассом int
# В третьем случае мне нужно убедиться, что data относится к классу,
# с котором можно совершать математические дейтсвия

num = 2 + 2 * 2
digit = 36 / 6
print(num, digit)
print(num == digit)
print(num is digit)
print('___________________________')
# Оператор is сравнивает объекты по их классам,
# т.к. они находятся в разном месте памяти. Получаем False.

a = 5
print(a, id(a), sep='->')
a += 1
print(a, id(a), sep='->')
print('___________________________')
# Мы смогли прибавить 1 к 5, однако адреса в ОЗУ различаются.
# Числа - неизменяемый тип данных. Каждый раз получая новое число,
# Python создаёт новое место в памяти, а переменная просто на него указывает.
# Т.е., взяли стикер, зачеркнули старый адрес памяти, написали новый.

# txt = 'Hello world!'
# txt[5] = '_'
# Получим ошибку, т.к. строка является объектом неизменямого типа данных.
txt = 'Hello world!'
print(txt, id(txt), sep='->')
txt = txt.replace(' ', '_')
print(txt, id(txt), sep='->')
print('___________________________')
# Мы всё равно получили два объкта с разным размещением в ОЗУ.
# Строгая динамическая типизация и невозможность заменить неизменяемый объект.

a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c), sep='->')
a = b + c
print(a, id(a), b, id(b), c, id(c), sep='->')
print('___________________________')
# До математической операции обе переменные а и c ссылались на один объект в ОЗУ.
# После операции сложения, т.к. у нас объект неизменяем, переменная а указывает на новое место в ОЗУ,
# При этом переменная с как указывала на 2-ку, так и указывает.

x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print('___________________________')
# print(hash(my_list)) - получим ошибку, т.к. list изменяемый
# Как видите нижняя строка кода вызывает ошибку TypeError: unhashable type:
# 'list' Если вдруг забыли изменяемый объект или нет, просто попробуйте
# получить его хеш.

# ЗАДАНИЕ
# Напишите небольшую программу, которая
# запрашивает у пользователя любой текст
# и выводит о нём следующую информацию:
# ✔ тип объекта;
# ✔ адрес объекта в оперативной памяти;
# ✔ хеш объекта.

text = input('Input your text here:\n')


def get_info_text():
    typ = type(text)
    iden = id(text)
    _hash = hash(text)
    print(f'Тип ваших данных {typ}\n'
          f'Идентификатор в ОЗУ -> {iden}\n'
          f'Хэш-сумма: {_hash}')
    print('___________________________')


get_info_text()