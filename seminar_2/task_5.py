# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a, b, c = map(int, input('Введите три коэффициента уравнения через проблел: \n').split())

d = b**2 - 4*a*c
res = ''

if d > 0:
    x1 = (-b-d**0.5) / (2*a)
    x2 = (-b+d**0.5) / (2*a)
    res: str = f'Уравнение имеет два корня: {x1}, {x2}'
elif d == 0:
    x = -b / (2*a)
    res: str = f'Уравнение имеет один корень: {x}'
else:
    d = complex(d, 0)
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    res: str = f'Уравнение имеет два комплексных корня: {x1}, {x2}'

print(res)