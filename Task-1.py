from random import *

def print_matrix(matrix:list):
    for line in matrix:
        print(*line)

def function(list_:list):
    minimum = 10**11
    index = []
    jndex = []
    for i in range(len(list_)):
        for j in range(len(list_[i])):
            if list_[i][j] < minimum:
                minimum = list_[i][j]
                index = []
                jndex = []
                index.append(i+1)
                jndex.append(j+1)
            elif list_[i][j] == minimum:
                index.append(i+1)
                jndex.append(j+1)
    return [minimum, index, jndex]

matrix_A = [[randint(-10,10) for _ in range(10)] for _ in range(5)]
matrix_B = [[randint(-10,10) for _ in range(4)] for _ in range(10)]
minimum_A = function(matrix_A)
minimum_B = function(matrix_B)
print('Матрица А')
print_matrix(matrix_A)
print(f'Наименьший элемент матрицы А = {minimum_A[0]} , находится в столбцах {minimum_A[2]} и строках {minimum_A[1]}')
print('Матрица B')
print_matrix(matrix_B)
print(f'Наименьший элемент матрицы B = {minimum_B[0]} , находится в столбцах {minimum_B[2]} и строках {minimum_B[1]}')