from typing import Type


class MatrixError(Exception):
    pass


class MatrixConsistencyError(MatrixError):
    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    def __str__(self):
        return 'Матрицы должны быть одинаковой длины.'


class MatrixAdditionError(MatrixError):
    def __init__(self, self_rows: int, self_cols: int, other_rows: int, other_cols: int):
        self.self_rows = self_rows
        self.self_cols = self_cols
        self.other_rows = other_rows
        self.other_cols = other_cols

    def __str__(self):
        return f'Матрица не может быть добавлена: строки и столбцы обеих матриц должны быть равны!\n' \
               f'Ряды матриц: {self.self_rows}, {self.other_rows}.\n' \
               f'Столбцы матриц: {self.self_cols}, {self.other_cols}.'


class MatrixMultiplyError(MatrixError):
    def __init__(self, self_cols: int, other_rows: int):
        self.self_cols = self_cols
        self.other_rows = other_rows

    def __str__(self):
        return f'Матрицы не могут быть перемножены: ' \
               f'количество столбцов первой матрицы ({self.self_cols}) ' \
               f'должно быть равно количеству строк во второй матрице ({self.other_rows})!'


class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __new__(cls, matrix: list[list[int]]):
        if type(matrix) is not list:
                raise TypeError(f'Входящая матрица должна быть списком. Вы указали: {type(matrix)}')

        if len({len(row) for row in matrix}) != 1:
            raise MatrixConsistencyError(matrix)

        return super().__new__(cls)

    def concat_rows(self):
        return [item for row in self.matrix for item in row]

    def __is_lengths_equal(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def __eq__(self, other):
        if self.__is_lengths_equal(other):
            return sorted(self.concat_rows()) == sorted(other.concat_rows())
        return False

    def __lt__(self, other):
        if self.rows * self.cols < other.rows * other.cols:
            return True
        elif self.rows * self.cols > other.rows * other.cols:
            return False
        else:
            return sum(self.concat_rows()) < sum(other.concat_rows())

    def __le__(self, other):
        if self.rows * self.cols < other.rows * other.cols:
            return True
        elif self.rows * self.cols > other.rows * other.cols:
            return False
        else:
            return sum(self.concat_rows()) <= sum(other.concat_rows())

    def __add__(self, other):
        if self.__is_lengths_equal(other):
            sum_matrix = []
            for row_i in range(self.rows):
                sum_row = []
                for item_i in range(self.cols):
                    sum_row.append(self.matrix[row_i][item_i] + other.matrix[row_i][item_i])
                sum_matrix.append(sum_row)
            return Matrix(sum_matrix)
        else:
            raise MatrixAdditionError(self.rows, self.cols, other.rows, other.cols)

    def __mul__(self, other):
        if self.cols == other.rows:
            mul_matrix = []
            for row in self.matrix:
                mul_row = []
                for col_i in range(other.cols):
                    mul_row.append(sum(row[i] * other.matrix[i][col_i] for i in range(self.cols)))
                mul_matrix.append(mul_row)
            return Matrix(mul_matrix)
        else:
            raise MatrixMultiplyError(self.cols, other.rows)

    def __str__(self):
        max_length = max(map(lambda x: max(map(lambda y: len(str(y)), x)), self.matrix))
        output = ''
        for i in range(len(self.matrix)):
            output += '| '
            for j in range(len(self.matrix[i])):
                output += f'{self.matrix[i][j]:>{max_length}} '
            output += '|\n'
        return output

    def __repr__(self):
        return f'Matrix({self.matrix})'


if __name__ == '__main__':
    matrix_1 = Matrix([[444, 33, 1], [666, 55, 88]])
    matrix_2 = Matrix([[444, 33, 1], [666, 55, 88, 44]])
    print(matrix_1)