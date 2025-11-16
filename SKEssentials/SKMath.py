import functools
import math

def prod(*numbers):
    product = 1
    for n in numbers: product *= n
    return product

def near_int(number):
    return math.floor(number + 0.5)

def round(number, dp = None, sf = None):
    assert type(number) in (int, float), "Argument <number> must be a real number."
    assert dp is None or (type(dp) == int and sf is None), \
        "Argument <dp> must be an integer, and arguments <dp> and <sf> are mutually exclusive."
    assert sf is None or (type(sf) == int and dp is None), \
        "Argument <sf> must be an integer, and arguments <dp> and <sf> are mutually exclusive."

    if type(dp) == int:
        result = (number * 10 ** dp) // 1 / 10 ** dp
        if result % 1 == 0:
            return near_int(result)
        else: return result
    elif type(sf) == int:
        p = math.floor(math.log10(number))
        dp = sf + p - 1
        result = (number * 10 ** dp) // 1 / 10 ** dp
        if result % 1 == 0:
            return near_int(result)
        else: return result
    else:
        if number % 1 == 0:
            return near_int(number)
        return number

def short(number, dp = None, sf = None):
    assert type(number) in (int, float), "Argument <number> must be a real number."
    assert dp is None or (dp >= 0 and sf is None), \
        "Argument <dp> must be a non-negative integer, and arguments <dp> and <sf> are mutually exclusive."
    assert sf is None or (sf >= 0 and dp is None), \
        "Argument <sf> must be a non-negative integer, and arguments <dp> and <sf> are mutually exclusive."

    abs_number = abs(number)

    _map = {
        1_000_000: "million",
        1e+9 : "billion",
        1e+12 : "trillion",
        1e+15 : "quadrillion",
        1e+18 : "quintillion",
        1e+21 : "sextillion",
        1e+24 : "septillion",
        1e+27 : "octillion",
        1e+30 : "nonillion",
        1e+33 : "decillion",
    }

    divisor = 1
    suffix = ""
    for k, e in _map.items():
        if k <= abs_number < 1_000 * k:
            divisor = k
            suffix = e
            break

    if suffix:
        if (number / divisor) % 1 == 0:
            return f"{round(number // divisor, dp=dp, sf=sf)} {suffix}"
        else: return f"{round(number / divisor, dp = dp, sf = sf)} {suffix}"
    else:
        return round(number, dp = dp, sf = sf)

class Matrix:
    def __init__(self, array = None, rows = None, columns = None, rep_num = None):
        if array or (not array and not rows and not columns):
            assert rows == columns == rep_num is None, (
                "You must either define the who array, or the number of rows and columns, "
                "which may include a repeating number."
            )
            self.array = [list(P) for P in array]
            self.rows = len(array)
            self.columns = len(array[0])

            for _list in array:
                if len(_list) != self.columns:
                    raise ValueError("Matrix must have the same number of rows across all columns.")
        else:
            assert array is None, (
                "You must either define the who array, or the number of rows and columns, "
                "which may include a repeating number."
            )
            rep_num = rep_num or 0
            self.rows = rows
            self.columns = columns
            self.array = [[rep_num for _ in range(columns)] for _ in range(rows)]
    def __str__(self):
        n = [0 for _ in range(self.columns)]
        for row, _list in enumerate(self.array):
            for col, e in enumerate(_list):
                if len(str(e)) > n[col]: n[col] = len(str(e))

        string = ""
        for row, _list in enumerate(self.array):
            ss = ""
            for col, e in enumerate(_list):
                if col != 0: ss += " "
                ss += str(e).rjust(n[col])
            if row == 0:
                ss = "┌ " + ss + " ┐"
            elif row == self.rows - 1:
                ss = "\n└ " + ss + " ┘"
            else:
                ss = "\n│ " + ss + " │"
            string += ss
        return string

    def row(self, index):
        return self.array[index]
    def column(self, index):
        result = [None for _ in range(self.columns)]
        for i, _list in enumerate(self.array):
            result[i] = _list[index]
        return result

    def __add__(self, other):
        assert isinstance(other, Matrix), "Argument <other> must be a matrix."
        assert self.rows == other.rows and self.columns == other.columns, \
            "Matrices must have the same size in order to be added."

        result = Matrix(rows = self.rows, columns = self.columns)
        for i in range(self.columns):
            for j in range(self.rows):
                result.array[i][j] = self.array[i][j] + other.array[i][j]
        return result

    def __mul__(self, other):
        assert type(other) in (int, float, Matrix), \
            "Argument <other> must be a matrix or a real number."

        if type(other) == Matrix:
            assert self.columns == other.rows, (
                "Matrix <self> must have the same number of columns as the number of "
                "rows of matrix <other> in order to be multiplied."
            )
            result = Matrix(rows = self.rows, columns = other.columns)
            for i in range(other.columns):
                for j in range(self.rows):
                    result.array[i][j] = \
                        sum([self.array[i][n] * other.array[n][j] for n in range(self.columns)])
            return result
        else:
            result = Matrix(rows = self.rows, columns = self.columns)
            for i in range(self.columns):
                for j in range(self.rows):
                    result.array[i][j] = self.array[i][j] * other
            return result
    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return self * -1
    def __sub__(self, other):
        return self + (-other)

    def delete_row(self, index):
        result = Matrix(self.array)
        result.array.pop(index)
        result.rows -= 1
        return result
    def delete_column(self, index):
        result = Matrix(self.array)
        for _list in result.array:
            _list.pop(index)
        result.columns -= 1
        return result

    def det(self):
        assert self.rows == self.columns, "Matrix <self> has no determinant."

        if self.rows == 1: return self.array[0][0]
        elif self.rows == 2: return self.array[0][0] * self.array[1][1] - self.array[0][1] * self.array[1][0]
        else:
            return sum([
                (-1) ** j * self.array[0][j] * self.delete_row(0).delete_column(j).det()
                for j in range(self.rows)
            ])

    def matrix_of_minors(self):
        assert self.rows == self.columns, "Matrix <self> has no matrix of minors."
        result = Matrix(rows = self.rows, columns = self.columns)
        for i, _list in enumerate(result.array):
            for j, _ in enumerate(_list):
                result.array[i][j] = self.delete_row(i).delete_column(j).det()
        return result
    def checker(self):
        result = Matrix(self.array)
        for i in range(self.columns):
            for j in range(self.rows):
                if (i + j) % 2 == 1:
                    result.array[i][j] *= -1
        return result
    def T(self):
        result = Matrix(rows = self.columns, columns = self.rows)
        for i, _list in enumerate(result.array):
            for j, _ in enumerate(_list):
                result.array[i][j] = self.array[j][i]
        return result

    def inverse(self):
        assert self.rows == self.columns, "Matrix <self> has no inverse."

        if self.rows == 1: return Matrix([[self.array[0][0]]])
        elif self.rows == 2:
            return (1 / self.det()) * Matrix([[self.array[1][1], -self.array[0][1]],
                [-self.array[1][0], self.array[0][0]]])
        else:
            return (1 / self.det()) * self.matrix_of_minors().checker().T()


def IMatrix(n):
    result = Matrix(rows = n, columns = n)
    for i in range(n):
        result.array[i][i] = 1
    return result


A = Matrix([[1, 2, 0], [4, 0, 6], [0, 8, 9]])
A *= A.inverse()
print(A)