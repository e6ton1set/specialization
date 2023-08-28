# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal as dec
import math as ma

dec.getcontext().prec = 42
PI: dec.Decimal = dec.Decimal(ma.pi)


def get_area_and_length_circle() -> dec.Decimal:
    d = input('Please enter a D (over 0 and less than 1000):\n')
    return dec.Decimal(d)


d = get_area_and_length_circle()
length: dec.Decimal = d*PI
area: dec.Decimal = (d/2)**2*PI

print('lenth: ', length, 'area: ', area, sep='\n')
