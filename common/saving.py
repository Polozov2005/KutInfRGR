import xlsxwriter as wr # Для записи данных в Excell таблицу
import numpy as np # Для работы с матрицами
import pandas as pd # Для работы с матрицами

# Запись значений напряжений узловых потенциалов в файл U.xlsx
def X(X_list):
    df_X = pd.DataFrame(data=X_list)
    df_X = df_X.iloc[1:]
    df_X.columns = ['X, кВ']
    writer = pd.ExcelWriter('excell_tables/X.xlsx', engine='xlsxwriter')
    df_X.to_excel(writer, 'X')
    writer._save()