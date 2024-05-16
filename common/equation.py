import matrix_expression as me
import numpy as np

# Расчёт значений узловых потенциалов всей схемы
def U(A, Y, I, E):
    LEFT = me.matrix_multiplication(A, Y)
    LEFT = me.matrix_multiplication(LEFT, me.transposition(A))

    RIGHT = me.matrix_multiplication(Y, E)
    RIGHT = me.addition(I, RIGHT)
    RIGHT = me.matrix_multiplication(A, RIGHT)
    RIGHT = me.scalar_multiplication(-1, RIGHT)

    matrix = me.gauss(LEFT, RIGHT)

    if isinstance(matrix, int) and matrix == 0:
        dictionary = {
            'list':0,
            'matrix':0
        }

    else:
        rowcount = matrix.shape[0]

        list = np.zeros([rowcount + 1], dtype=np.complex64)
        for i in range(1, rowcount + 1):
            list[i] = matrix[i - 1, 0]

        dictionary = {
            'list':list,
            'matrix':matrix
        }

    return dictionary

# Расчёт значений узловых потенциалов в точках X
def X(U):
    list = np.zeros([10 + 1], dtype=np.complex64)

    list[ 1] = U[11]
    list[ 2] = U[16]
    list[ 3] = U[ 9]
    list[ 4] = U[10]
    list[ 5] = U[ 7]
    list[ 6] = U[ 8]
    list[ 7] = U[ 3]
    list[ 8] = U[ 4]
    list[ 9] = U[ 1]
    list[10] = U[ 2]
    list[11] = U[17]

    dictionary = {
        'list':list
    }

    return dictionary