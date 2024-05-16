import numpy as np # Для создания матриц

# Сложение матриц
def addition(A, B):
    if A.shape != B.shape:
        print('Ошибка при сложении: матрицы должны быть одного размера')
    else:
        C = np.copy(A)
        C = C.astype('complex64')

        D = np.copy(B)
        D = D.astype('complex64')

        rowcount = C.shape[0]
        columncount = C.shape[1]

        result = np.zeros([rowcount, columncount], dtype=np.complex64)

        for i in range(rowcount):
            for j in range(columncount):
                result[i, j] = C[i, j] + D[i, j]

        return result

# Умножение матриц
def matrix_multiplication(A, B):
    if A.shape[1] != B.shape[0]:
        print('Ошибка при умножении: число столбцов первого множителя должно совпадать', 
              'с числом строк второго множителя')   
    else:
        C = np.copy(A)
        C = C.astype('complex64')

        D = np.copy(B)
        D = D.astype('complex64')

        rowcount = C.shape[0]
        columncount = D.shape[1]

        result = np.zeros([rowcount, columncount], dtype=np.complex64)

        for i in range(rowcount):
            for k in range(columncount):
                for j in range(C.shape[1]):
                    result[i, k] = result[i, k] + C[i, j] * B[j, k]

        return result
    
# Умножение матрицы на скаляр
def scalar_multiplication(a, A):
    C = np.copy(A)
    C = C.astype('complex64')

    rowcount = C.shape[0]
    columncount = C.shape[1]

    for i in range(rowcount):
        for j in range(columncount):
            C[i, j] = a * C[i, j]

    result = C
    return result


# Транспонирование
def transposition(A):
    T = np.copy(A)
    T = T.astype('complex64')

    rowcount = T.shape[1]
    columncount = T.shape[0]

    result = np.zeros([rowcount, columncount], dtype=np.complex64)

    for i in range(rowcount):
        for j in range(columncount):
            result[i, j] = T[j, i]

    return result

# Решение СЛАУ методом Гаусса
def gauss(A, B):
    errorcount = 0

    if A.shape[0] != A.shape[1]:
        print('Левая часть уравнения должна быть квадратной матрицей')
        errorcount += 1
    
    if B.shape[1] != 1:
        print('Правая часть уравнения должна быть столбцом')
        errorcount += 1
    
    if A.shape[0] != B.shape[0]:
        print('Количества строк левой и правой матриц должны совпадать')
        errorcount += 1

    if errorcount == 0:
        C = np.copy(A)
        C = C.astype('complex64')

        D = np.copy(B)
        D = D.astype('complex64')

        rowcount = C.shape[0]
        X = np.zeros([rowcount, 1], dtype=np.complex64)

        # Прямой ход
        for k in range(rowcount - 1):
            if C[k, k] == 0:
                print('В ходе решения на главной диагонали оказался ноль - система не совместна')
                errorcount += 1
                
                result = 0
            else:
                for i in range(k+1, rowcount):
                    coefficient = C[i, k] / C[k, k]
                    C[i, k] = 0

                    for j in range(k+1, rowcount):
                        C[i, j] += -C[k, j] * coefficient
                    
                    D[i] += -D[k] * coefficient

        # Обратный ход
        if errorcount == 0:
            if C[rowcount - 1, rowcount - 1] == 0:
                print('В ходе решения на главной диагонали оказался ноль - система не совместна')
                errorcount += 1

                result = 0
            else:
                X[rowcount - 1] = D[rowcount - 1] / C[rowcount - 1, rowcount - 1]
                for i in range(rowcount - 2, 0 - 1, -1):
                    S = 0

                    for j in range(i+1, rowcount):
                        S += C[i, j] * X[j]

                    X[i] = (D[i] - S) / C[i, i]


                result = X
    
    return result