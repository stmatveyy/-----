
import copy
import numpy

from exeptions import MatrixExeption


class Matrix(list):
    def __init__(self, *args) -> None:

        rows = int(input('Введите горизонтальную размерность матрицы: '))
        cols = int(input('Введите вертикальную размерность матрицы: '))
        if rows <= 0 or cols <= 0:
            raise MatrixExeption("Недопустимая размерность! \n")
        else:
            self.rows = rows
            self.cols = cols
            self.mas = []
            for i in range(0, cols):
                user_value_list = []

                for j in range(0, rows):
                    user_value = float(input('Введитe элемент строки: '))
                    user_value_list.append(user_value)
                self.mas.append(user_value_list)

                print('\t------переход на строку------\t')

    def multiplication_by_num(self, rows, cols, *args) -> list[list[float]]:

        '''Умножить матрицу на число multiplicator'''
        multiplicator = float(input("Введите множитель: "))
        return [[self.mas[i][j] * multiplicator for j in range(rows)]
                for i in range(cols)]

    def multiplication_matrices(self, cols) -> list[list[float]]:

        '''Умножить две матрицы'''

        matrix2 = Matrix()
        if cols != matrix2.cols:
            raise MatrixExeption("Неверная размерность матриц!\n")
        else:
            return numpy.matmul(self.mas, matrix2.mas)

    def matrices_adition(self, rows, cols) -> list[list[float]]:
        '''Сложить две матрицы'''
        matrix2 = Matrix()
        if (rows != matrix2.rows) or (cols != matrix2.cols):
            raise MatrixExeption("Неверная размерность! ")

        return [[self.mas[i][j] + matrix2.mas[i][j] for j in range(rows)]
                for i in range(cols)]

    def transpond(self, rows, cols) -> list[list[float]]:
        '''Транспонировать матрицу'''
        if rows != cols:
            raise MatrixExeption("Неверная размерность! ")
        else:
            return [[self.mas[j][i] for j in range(cols)] for i in range(rows)]

    def addition(self, rows, cols) -> list[list[float]]:
        number = float(input("Введите слагаемое: "))
        if ValueError:
            raise MatrixExeption("Недопустимое слагаемое! ")
        else:
            return [[self.mas[i][j] + number for j in range(rows)]
                    for i in range(cols)]

    def replacing_rows(self, rows) -> list[list[float]]:

        '''1-й тип элементарных преобразований матриц.

        Меняет местами строки, номера которых определяет пользователь.'''

        row_from = int(input('\nВведите 1 строку: ')) - 1
        row_to = int(input('\nВведите 2 строку: ')) - 1

        if (0 > row_from > rows) or (0 > row_to > rows):
            raise MatrixExeption("Неверно введены строки!\n")

        else:
            temp = self.mas[row_from]
            self.mas[row_from] = self.mas[row_to]
            self.mas[row_to] = temp
            return self.mas

    def replacing_cols(self, rows, cols, *args) -> list[list[float]]:
        '''1-й тип элементарных преобразований матрицы.

        Меняет местами столбцы, номера которых определяет пользователь.'''

        col_from = int(input('\nВведите 1 столбец: ')) - 1
        col_to = int(input('\nВведите 2 столбец: ')) - 1

        if (0 > col_from > cols):
            raise MatrixExeption("Неверно введены столбцы!\n")

        else:
            temp = self.mas[col_from]
            self.mas[col_from] = self.mas[col_to]
            self.mas[col_to] = temp
            return self.mas

    def linear_add(self, rows, cols) -> list[list[float]]:

        first_row = int(input('Введите 1 строку: ')) - 1
        second_row = int(input('Введите 2 строку: ')) - 1
        multiplicator = float(input('Введите множитель 2 строки: '))

        if (0 > first_row > rows) or (0 > second_row > rows):
            raise MatrixExeption("Неверно введены строки!\n")

        else:
            return [self.mas[first_row][i] + self.mas[second_row][i]
                    * multiplicator for i in range(cols)]

    def row_multiplication(self, rows) -> list[list[float]]:
        '''2-й тип элементарных преобразований матрицы

        Умножает строку, выбранную пользователем, на число
        '''
        row_num = int(input("Введите строку: ")) - 1
        multiplicator = float(input("Введите множитель: "))

        if row_num <= 0 or row_num + 1 > rows:
            raise MatrixExeption("Недопустимая строка! \n")
        else:
            for i in range(rows):
                self.mas[row_num][i] *= multiplicator
            return self.mas

    def col_multiplication(self, cols, *args) -> list[list[float]]:
        '''2-й тип элементарных преобразований матрицы.

        Умножает столбец, выбранный пользователем, на число.'''

        col_num = int(input("Введите столбец: ")) - 1
        multiplicator = float(input("Введите множитель: "))

        if col_num <= 0 or col_num + 1 > cols:
            raise MatrixExeption("Недопустимый столбец! \n")
        else:
            for i in range(cols):
                self.mas[i][col_num] *= multiplicator
            return self.mas

    def linear_addition(self, cols) -> list[list[float]]:

        '''3-й тип элементарных преобразований матрицы.

        Складывает со строкой 1, выбранной пользователем,
        строку 2 умноженную на заданное число.
        '''
        col_from = int(input("Введите первую строку: ")) - 1
        col_to = int(input("Введите вторую строку: ")) - 1
        multiplicator = float(input("Введите множитель второй строки: "))

        if col_from < cols or col_to < cols:
            raise MatrixExeption("Недопустимая строка! ")
        else:
            return [self.mas[col_from][i] + self.mas[col_to][i]
                    * multiplicator for i in range(cols)]

    def minor(self, rows, i, j):
        minor_mas = copy.deepcopy(self.mas)
        del minor_mas[i]
        for i in range(rows-1):
            del minor_mas[i][j]
        return minor_mas

    def determinator(self, rows, cols) -> int:

        if rows != cols:
            raise MatrixExeption("Недопустимый размер матрицы! \n")
        elif rows == 1:
            return self.mas[0][0]
        elif rows == 2:
            return self.mas[0][0]*self.mas[1][1]-self.mas[0][1]*self.mas[1][0]
        else:
            return round(numpy.linalg.det(self.mas))

    def reverse_matrix(self, rows, cols) -> list[list[float]]:

        if rows != cols:
            raise MatrixExeption("Матрица не квадратная! ")
        else:
            numpy.linalg.inv(self.mas)

    def rank(self):
        numpy.linalg.matrix_rank(self.mas)
