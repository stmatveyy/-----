
import copy
import sys
import numpy as np
from exeptions import MatrixExeption

class Matrix():
    def __init__(self, *args) -> None:

        rows = int(input('Введите горизонтальную размерность матрицы: '))
        cols = int(input('Введите вертикальную размерность матрицы: '))
        if rows <= 0 or cols <= 0:
            raise MatrixExeption("Недопустимая размерность! \n")
        
        else:
            self.rows = rows ## m
            self.cols = cols ## n
            self.mas = []
            for i in range (0,cols):
                user_value_list = []

                for j in range (0,rows):    
                    user_value = float(input('Введитe элемент строки: '))
                    user_value_list.append(user_value)
                self.mas.append(user_value_list)

                print('\t------переход на строку------\t')

    def multiplication_by_num(self, rows, cols, *args) -> list[list[float]]:

        '''Умножить матрицу на число multiplicator'''
        multiplicator = float(input("Введите множитель: "))
        return [[self.mas[i][j] * multiplicator for j in range(rows)] for i in range(cols)]
    
    def multiplication_matrices(self,cols) -> list[list[float]]:

        '''Умножить две матрицы'''
        
        matrix2 = Matrix()
        if cols != matrix2.cols:
            raise MatrixExeption("Неверная размерность матриц!\n")
        else:
            return np.matmul(self.mas,matrix2.mas)

    def matrices_adition(self,rows,cols) -> list[list[float]]:
        '''Сложить две матрицы'''
        matrix2 = Matrix()
        if (rows != matrix2.rows) or (cols != matrix2.cols):
            raise MatrixExeption("Неверная размерность! ")
        
        return [[self.mas[i][j] + matrix2.mas[i][j] for j in range(rows)] for i in range(cols)]

    def transpond(self, rows, cols) -> list[list[float]]:
        '''Транспонировать матрицу'''
        if rows != cols:
            raise MatrixExeption("Неверная размерность! ")
        else:
            return [[self.mas[j][i] for j in range(cols)] for i in range(rows)]
    
    def addition(self,rows,cols, *args) -> list[list[float]]:
        number = float(input("Введите слагаемое: "))
        if ValueError:
            raise MatrixExeption("Недопустимое слагаемое! ")
        else:
            return [[self.mas[i][j] + number for j in range(rows)] for i in range(cols)]

    def replacing_rows(self,rows,cols, *args) -> list[list[float]]:

        '''1-й тип элементарных преобразований матриц.

        Меняет местами строки, номера которых определяет пользователь.'''
        
        row_from = int(input('\nВведите 1 строку: ')) -1
        row_to = int(input('\nВведите 2 строку: ')) -1
        
        if (0 > row_from > rows) or (0 > row_to > rows):
            raise MatrixExeption("Неверно введены строки!\n")
        
        else:
            temp = self.mas[row_from]
            self.mas[row_from] = self.mas[row_to]
            self.mas[row_to] = temp
            return self.mas

    def replacing_cols(self,rows,cols, *args) -> list[list[float]]:
        '''1-й тип элементарных преобразований матрицы.
    
        Меняет местами столбцы, номера которых определяет пользователь.'''

        col_from = int(input('\nВведите 1 столбец: ')) -1 
        col_to = int(input('\nВведите 2 столбец: ')) -1

        if (0 > col_from > rows):
            raise MatrixExeption("Неверно введены столбцы!\n")
        
        else:
            temp = self.mas[col_from]
            self.mas[col_from] = self.mas[col_to]
            self.mas[col_to] = temp
            return self.mas
    
    def linear_add(self,rows,cols, *args) -> list[list[float]]:

        first_row = int(input('Введите 1 строку: ')) -1
        second_row = int(input('Введите 2 строку: ')) -1
        multiplicator = float(input('Введите множитель 2 строки: '))

        if (0 > first_row > rows) or (0 > second_row > rows):
            raise MatrixExeption("Неверно введены строки!\n")
        else:
            return [self.mas[first_row][i] + self.mas[second_row][i] * multiplicator for i in range(cols)]
        
    def row_multiplication(self,rows,*args) -> list[list[float]]:
        '''2-й тип элементарных преобразований матрицы

        Умножает строку, выбранную пользователем, на число
        '''
        row_num = int(input("Введите строку: ")) -1 
        multiplicator = float(input("Введите множитель: "))

        if row_num <=0 or row_num + 1> rows:
            raise MatrixExeption("Недопустимая строка! \n")
        else:
            for i in range(rows):
                self.mas[row_num][i] *= multiplicator
            return self.mas

    def col_multiplication(self,cols, *args) -> list[list[float]]:
        '''2-й тип элементарных преобразований матрицы.
    
        Умножает столбец, выбранный пользователем, на число.'''

        col_num = int(input("Введите столбец: ")) -1 
        multiplicator = float(input("Введите множитель: "))

        if col_num <=0 or col_num + 1> cols:
            raise MatrixExeption("Недопустимый столбец! \n")
        else:
            for i in range(cols):
                self.mas[i][col_num] *= multiplicator
            return self.mas
        
    def linear_addition(self, cols) -> list[list[float]]:
            
            '''3-й тип элементарных преобразований матрицы.
    
        Складывает со строкой 1, выбранной пользователем, строку 2 умноженную на заданное число.
        '''
            col_from = int(input("Введите первую строку: ")) -1
            col_to = int(input("Введите вторую строку: ")) -1
            multiplicator = float(input("Введите множитель второй строки: "))

            if col_from < cols or col_to < cols:
                raise MatrixExeption("Недопустимая строка! ")
            else:
                return [self.mas[col_from][i] + self.mas[col_to][i] * multiplicator for i in range(cols)]
    
    def minor(self,rows, i, j):
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
            return round(np.linalg.det(self.mas))
            
# def minor(matrix, i, j,m,n ):
#     '''Находит минор матрицы. 
    
#     Работает только внутри функций. \nНеобходимы параметры i и j (индексы)
#     Используйте вложенный цикл for ... in range
#     Возвращает М
#     '''
#     global M
#     M = copy.deepcopy(matrix)  
#     m = len(matrix)
#     n = len(matrix[0])
#     del M[i]
#     m = len(matrix)
#     n = len(matrix[0])
#     for i in range(m-1):
#         del M[i][j]
    
# def determinator(matrix):
#     '''Находит определитель матрицы.
    
#     Матрица должна быть квадратной.
#     Возвращает det
#     '''
#     global det
#     m = len(matrix)
#     n = len(matrix[0])
#     if m != n:
#         print('///Не квадратная матрица!')
#     if n == 1:
#         return matrix[0][0]
#     signum = 1
#     det = 0
#     # разложение по первой строке
#     for j in range(n):
#         det += matrix[0][j]*signum*determinator( minor(matrix, 0, j,m,n) ) 
#         signum *= -1
#     return det

def reverse_matrix(matrix):
    '''Находит обратную матрицу.
    
    Возвращает result_matrix
    '''
    global dop
    global dop_matrix
    global result_matrix
    result_matrix = []
    dop_matrix_st = []
    dop_matrix = []
    m = len(matrix)
    n = len(matrix[0])
    if m != n:
        print('------Матрица не квадратная!------')
    else:
        signum = 1
        dop = 0
        a = 2
        # разложение по первой строке
        for i in range(n):
            dop_matrix_st = []
            for j in range(m):
                a +=1
                if (i + j) %2 == 1:
                    signum =(-1)
                else:
                    signum = 1
                dop = signum*determinator(minor(matrix, i, j,m,n)) 
                dop_matrix_st.append(dop)
            dop_matrix.append(dop_matrix_st)
        transpond(dop_matrix,m,n)
        a = trans_matrix
        b = determinator(matrix)
        r ='RESULT'
        r1 = r.center(len(r)+22,'=')
        print('\n')
        print('\t',f'{r1}','\t')
        
        for row in a:
            print(("  {:^5}  "*n).format(*row))
        print(' '*(10*n-3),'|* 1/',b,'|')
    


def rang(matrix,m,n): #####хуйня с индесками
    '''Находит ранг матрицы.
    
    Возвращает rangg
    '''
    global rank
    if matrix[0][0] == 0:
        rank = 0
        return rank
    else:
        rank = 0
        i = 1
        j = 1
        
        while rank <= m and rank <= n:
            for i in range(n):
                for j in range(n):
                    mat = matrix
                    determinator(minor(mat,i,j,m,n))
                    if det != 0:
                        rank +=1
        rank = rank/m -1
        
        
        return print(rank)
####### MAIN ########
# def main_f():

#     print('Калькулятор матриц mcalc // ver1.6\t\n ')
#     print('\t\tВыберите операцию:\t ')
#     print('     1 --- умножить матрицу на число \n \
#     2 --- умножить 2 матрицы \n \
#     3 --- сложить 2 матрицы \n \
#     4 --- транспонировать матрицу \n \
#     _______элементарные преобразования______ \n \
#     5 --- поменять местами 2 столбца \n \
#     6 --- поменять местами 2 строки \n \
#     7 --- умножить строку на число \n \
#     8 --- умножить столбец на число \n \
#     9 --- сложить со строкой I строку II умноженную на число ')
#     print('     ______________________________________')
#     print('     10 --- найти определитель квадратной матрицы \n \
#     11 -- найти обратную матицу \n ')

#     choose = int(input('Выбор: '))
#     if choose == 1:
#         creating()
#         x = int(input('Введите множитель: '))
#         multiplication_simple(matrix,x)
#         for i in range (-1,m-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 2:
#         double_creating()
#         multiplication_hard(matrix1,matrix2)
#         for i in range (-1,m1-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 3:
#         double_creating()
#         addition(matrix1,matrix2)
#         for i in range (-1,m1-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 4:
#         print('///Помните, матрица должна быть квадратной')
#         creating()
#         for i in range (-1,m-1):
#             i += 1
#             print(trans_matrix[i], '\n')
#     elif choose == 5:
#         creating()
#         replacing_cols(matrix)
#         for i in range (-1,m-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 6:
#         creating()
#         replacing_rows(matrix)
#         for i in range (-1,m-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 7:
#         creating()
#         row_multiplication(matrix)
#         for i in range (-1,m-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 8:
#         creating()
#         col_multiplication(matrix)
#         for i in range (-1,m-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 9:
#         creating()
#         linear_add(matrix)
#         for i in range (-1,m-1):
#             i += 1
#             print(result_matrix[i], '\n')
#     elif choose == 10:
#         print('///Помните, матрица должна быть квадратной')
#         creating()
#         determinator(matrix)
#         print(det)
#     elif choose == 11:
#         try:
#             creating()
#             reverse_matrix(matrix)
#         except:
#             print('Что-то пошло не так!')

# print('\nНажмите Enter для выхода.')
# try:
#     for i in range(100):
#         main_f()
# except ValueError:
#     print('Программа приостановлена.')
#     sys.exit(0)
    