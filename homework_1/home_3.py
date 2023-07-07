# Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

a, b, c = int(input('Сторона a: \n')),int(input('Сторона b: \n')),int(input('Сторона c: \n'))
result = '{}'
type_triangle = '{}'
flag = True

if a > b + c or b > c + a or c > b + a:
    result = result.format('Треугольник не существует.')
    flag = False
else:
    result = result.format('Треугольник существует.')
    if a == b == c:
        type_triangle = type_triangle.format('Он является равносторонним.')
    elif a != b != c:
        type_triangle = type_triangle.format('Он является разносторонним.')
    else:
        type_triangle = type_triangle.format('Он является равнобедренным.')

print(result)
print(type_triangle if flag else 'У несуществующего треугольника нет вида.')
