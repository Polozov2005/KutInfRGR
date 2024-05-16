# q = 19
# p = 31

import pandas as pd # Для чтения Excell таблиц
import numpy as np # Для создания матриц

# Инициализация значений источников ЭДС из файла E.xlsx
def E():
    filepath = 'excell_tables/E.xlsx'
    df = pd.read_excel(filepath)

    rowcount = df.shape[0]

    list = np.zeros([rowcount + 1], dtype=np.complex64)

    for i in range(1, rowcount + 1):
        list[i] = df.iloc[i - 1, 1]

    matrix = np.zeros([31, 1], dtype=np.complex64)

    matrix[0,  0] = list[1] # E1 -> Y1
    matrix[1,  0] = list[2] # E2 -> Y2
    matrix[16, 0] = list[3] # E3 -> Y17
    matrix[17, 0] = list[4] # E4 -> Y18

    dictionary = {
        'list':list,
        'matrix':matrix
    }

    return dictionary

# Инициализация значений проводимости из файла Y.xlsx
def Y():
    filepath = 'excell_tables/Y.xlsx'
    df = pd.read_excel(filepath)

    rowcount = df.shape[0]

    real = np.zeros([rowcount + 1], dtype=np.complex64)
    imag = np.zeros([rowcount + 1], dtype=np.complex64)

    for i in range(1, rowcount + 1):
        real[i] = df.iloc[i - 1, 1]

    for i in range(1, rowcount + 1):
        imag[i] = df.iloc[i - 1, 2]
    imag = imag * np.sqrt(-1, dtype=np.complex64)

    list = real + imag

    matrix = np.zeros([31, 31], dtype=np.complex64)

    for i in range(list.shape[0] - 1):
        matrix[i, i] = list[i + 1]

    dictionary = {
        'list':list,
        'matrix':matrix
    }

    return dictionary

# Инициализация матрицы соединений
def A():
    filepath = 'excell_tables/A.xlsx'
    df = pd.read_excel(filepath)
    df = df.fillna(0)

    matrix = df.iloc[0: , 1:].values
    matrix = matrix.astype('complex64')

    dictionary = {
        'matrix':matrix
    }
    
    return dictionary

# Инициализация значений источников тока
def I():
    filepath = 'excell_tables/I.xlsx'
    df = pd.read_excel(filepath)

    rowcount = df.shape[0]

    list = np.zeros([rowcount + 1], dtype=np.complex64)

    for i in range(1, rowcount + 1):
        list[i] = df.iloc[i - 1, 1]

    matrix = np.zeros([31, 1], dtype=np.complex64)

    dictionary = {
        'list':list,
        'matrix':matrix
    }

    return dictionary

A_matrix = A()['matrix']
print(A_matrix.shape)