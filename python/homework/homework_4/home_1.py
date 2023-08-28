# ✔Напишите функцию для транспонирования матрицы

matrix = [['b', 'a', 'b'],
          ['b', 'a', 'b'],
          ['b', 'a', 'b'],
          ['b', 'a', 'b']]

res_matrix = [['', '', '', ''],
              ['', '', '', ''],
              ['', '', '', '']]


def get_trans_matrix(data: list) -> list[str]:
    for a in range(len(data)):
        for b in range(len(data[0])):
            res_matrix[b][a] = data[a][b]

    for res in res_matrix:
        print(res)


get_trans_matrix(matrix)
