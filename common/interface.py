from tkinter import *
from tkinter import messagebox
from ctypes import windll
import numpy as np

import equation
import initialization
import saving

def interface_initialization():
    root.mainloop()

windll.shcore.SetProcessDpiAwareness(1) # Для отсутствия размытия интерфейса
root = Tk()
root.geometry("1600x900")
root.title("РГР")
root.resizable(False, False)

frm_scheme = Frame(
    root,
    background='red'
)
frm_scheme.place(
    x=0,
    y=0,
    width = 800,
    height = 900
)

frm_checkbutton = Frame(
    root,
)
frm_checkbutton.place(
    x=800,
    y=0,
    width = 800,
    height = 160
)

frm_Y = Frame(
    root,
)
frm_Y.place(
    x=800,
    y=160,
    width = 800,
    height = 160
)

frm_E = Frame(
    root,
)
frm_E.place(
    x=800,
    y=320,
    width = 800,
    height = 160
)

frm_solveandsave = Frame(
    root,
)
frm_solveandsave.place(
    x=800,
    y=480,
    width = 800,
    height = 100
)

frm_U = Frame(
    root,
)
frm_U.place(
    x=800,
    y=580,
    width = 800,
    height = 160
)

frm_X = Frame(
    root,
)
frm_X.place(
    x=800,
    y=740,
    width = 800,
    height = 160
)

### Схема
scheme = PhotoImage(file="gfx/scheme.png")

label_scheme = Label(
    frm_scheme,
    image=scheme
)

label_scheme.grid(
    row=0,
    column=0
)


### Выключатели

label_i_checkbutton = Label(
    frm_checkbutton,
    text='i'
)

label_i_checkbutton.grid(
    row=0,
    column=0,
)

label_B_checkbutton = Label(
    frm_checkbutton,
    text = 'B[i]'
)

label_B_checkbutton.grid(
    row=1,
    column=0,
)

list_label_checkbutton = [[]]
list_checkbutton = [[]]
list_enabled_checkbutton = [[]]
columncount_checkbutton = 0
for i in range(1, 24 +  1):
    if (11 <= i <= 20):
        list_label_checkbutton.append([])
        list_checkbutton.append([])
        list_enabled_checkbutton.append([])

    else:
        columncount_checkbutton += 1
        label_checkbutton = Label(
            frm_checkbutton,
            text=str(i)
        )

        list_label_checkbutton.append(label_checkbutton)

        list_label_checkbutton[i].grid(
            row = 0,
            column = columncount_checkbutton
        )

        enabled_checkbutton = IntVar(value=1)

        checkbutton = Checkbutton(
            frm_checkbutton,
            variable=enabled_checkbutton,
        )

        list_checkbutton.append(checkbutton)
        list_enabled_checkbutton.append(enabled_checkbutton)

        list_checkbutton[i].grid(
            row = 1,
            column = columncount_checkbutton,
        )

for i in range(columncount_checkbutton + 1):
    frm_checkbutton.columnconfigure(
        index=i,
        weight=1
    )

for i in range(1 + 1):
    frm_checkbutton.rowconfigure(
        index=i,
        weight=1
    )

### Y
Y_list = initialization.Y()['list']

for k in range(-((-len(Y_list)+1)//10)):
    label_i_Y = Label(
        frm_Y,
        text='i'
    )

    label_i_Y.grid(
        row=2*k,
        column=0,
    )

    label_Y = Label(
        frm_Y,
        text='Y[i], См'
    )

    label_Y.grid(
        row=2*k + 1,
        column=0,
    )

    for i in range(1, 10 + 1):
        delta = (len(Y_list) - 1) - 10*k
        if delta < 10:
            for j in range(1, delta + 1):
                label_count = Label(
                    frm_Y,
                    text=str(j + 10*k)
                )

                label_count.grid(
                    row=2*k,
                    column=j
                )
                
                label_Y_list = Label(
                    frm_Y,
                    text=str(Y_list[j + 10*k])
                )

                label_Y_list.grid(
                    row=2*k + 1,
                    column=j
                )

        else:
            label_count = Label(
                frm_Y,
                text=str(i + 10*k)
            )
            label_count.grid(
                row=2*k,
                column=i
            )
            
            label_Y_list = Label(
                frm_Y,
                text=str(Y_list[i + 10*k])
            )

            label_Y_list.grid(
                row=2*k + 1,
                column=i
            )

for i in range(11):
    frm_Y.columnconfigure(
        index=i,
        weight=1
    )

for i in range(6):
    frm_Y.rowconfigure(
        index=i,
        weight=1
    )

### E
E_list = initialization.E()['list']

for k in range(-((-len(E_list)+1)//10)):
    label_i_E = Label(
        frm_E,
        text='i'
    )

    label_i_E.grid(
        row=2*k,
        column=0,
    )

    label_E = Label(
        frm_E,
        text='E[i], кВ'
    )

    label_E.grid(
        row=2*k + 1,
        column=0,
    )

    for i in range(1, 10 + 1):
        delta = (len(E_list) - 1) - 10*k
        if delta < 10:
            for j in range(1, delta + 1):
                label_count = Label(
                    frm_E,
                    text=str(j + 10*k)
                )

                label_count.grid(
                    row=2*k,
                    column=j
                )
                
                label_E_list = Label(
                    frm_E,
                    text=str(E_list[j + 10*k])
                )

                label_E_list.grid(
                    row=2*k + 1,
                    column=j
                )

        else:
            label_count = Label(
                frm_E,
                text=str(i + 10*k)
            )
            label_count.grid(
                row=2*k,
                column=i
            )
            
            label_E_list = Label(
                frm_E,
                text=str(Y_list[i + 10*k])
            )

            label_E_list.grid(
                row=2*k + 1,
                column=i
            )

for i in range(5):
    frm_E.columnconfigure(
        index=i,
        weight=1
    )

for i in range(2):
    frm_E.rowconfigure(
        index=i,
        weight=1
    )


### Вывод кнопки для расчёта и сохранения
def click_solve():    
    A_matrix = initialization.A()['matrix']
    Y_matrix = initialization.Y()['matrix']
    I_matrix = initialization.I()['matrix']
    E_matrix = initialization.E()['matrix']

    if list_enabled_checkbutton[1].get() == 0:
        i = 5
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[2].get() == 0:
        i = 6
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[3].get() == 0:
        i = 9
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[4].get() == 0:
        i = 10
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[5].get() == 0:
        i = 13
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[6].get() == 0:
        i = 14
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[7].get() == 0:
        i = 15
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[8].get() == 0:
        i = 16
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[9].get() == 0:
        i = 29
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[10].get() == 0:
        i = 30
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[21].get() == 0:
        i = 7
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[22].get() == 0:
        i = 8
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[23].get() == 0:
        i = 21
        Y_matrix[i - 1, i - 1] = 0

    if list_enabled_checkbutton[24].get() == 0:
        i = 22
        Y_matrix[i - 1, i - 1] = 0

    U_list = equation.U(
        A=A_matrix,
        Y=Y_matrix,
        I=I_matrix,
        E=E_matrix
    )['list']

    if isinstance(U_list, int) and U_list == 0:
        messagebox.showerror(
            title='Ошибка в ходе решения уравнения',
            message='В ходе решения на главной диагонали оказался ноль - система не совместна'
        )
    else:
        U_list = np.round(U_list, 2)

        for k in range(-((-len(U_list)+1)//9)):
            label_i_U = Label(
                frm_U,
                text='i'
            )

            label_i_U.grid(
                row=2*k,
                column=0,
            )

            label_U = Label(
                frm_U,
                text='U[i], кВ'
            )

            label_U.grid(
                row=2*k + 1,
                column=0,
            )

            for i in range(1, 9 + 1):
                delta = (len(U_list) - 1) - 9*k
                if delta < 9:
                    for j in range(1, delta + 1):
                        label_count = Label(
                            frm_U,
                            text=str(j + 9*k)
                        )

                        label_count.grid(
                            row=2*k,
                            column=j,
                            sticky=NSEW
                        )
                        
                        label_U_list = Label(
                            frm_U,
                            text=str(U_list[j + 9*k])
                        )

                        label_U_list.grid(
                            row=2*k + 1,
                            column=j,
                            sticky=NSEW
                        )

                else:
                    label_count = Label(
                        frm_U,
                        text=str(i + 9*k)
                    )

                    label_count.grid(
                        row=2*k,
                        column=i,
                        sticky=NSEW
                    )
                    
                    label_U_list = Label(
                        frm_U,
                        text=str(U_list[i + 9*k])
                    )

                    label_U_list.grid(
                        row=2*k + 1,
                        column=i,
                        sticky=NSEW
                    )
            
        X_list = equation.X(U_list)['list']
        saving.X(X_list=X_list)

        for k in range(-((-len(X_list)+1)//9)):
            label_i_X = Label(
                frm_X,
                text='i'
            )

            label_i_X.grid(
                row=2*k,
                column=0,
            )

            label_X = Label(
                frm_X,
                text='X[i], кВ'
            )

            label_X.grid(
                row=2*k + 1,
                column=0,
            )

            for i in range(1, 9 + 1):
                delta = (len(X_list) - 1) - 9*k
                if delta < 9:
                    for j in range(1, delta + 1):
                        label_count = Label(
                            frm_X,
                            text=str(j + 9*k)
                        )

                        label_count.grid(
                            row=2*k,
                            column=j,
                            sticky=NSEW
                        )
                        
                        label_X_list = Label(
                            frm_X,
                            text=str(X_list[j + 9*k])
                        )

                        label_X_list.grid(
                            row=2*k + 1,
                            column=j,
                            sticky=NSEW
                        )

                else:
                    label_count = Label(
                        frm_X,
                        text=str(i + 9*k)
                    )

                    label_count.grid(
                        row=2*k,
                        column=i,
                        sticky=NSEW
                    )
                    
                    label_X_list = Label(
                        frm_X,
                        text=str(X_list[i + 9*k])
                    )

                    label_X_list.grid(
                        row=2*k + 1,
                        column=i,
                        sticky=NSEW
                    )

btn_solve = Button(
    frm_solveandsave,
    text='Рассчитать и сохранить',
    command=click_solve
)
btn_solve.grid(row=0, column=0)
frm_solveandsave.columnconfigure(index=0, weight=1)
frm_solveandsave.rowconfigure(index=0, weight=1)

### U
U_list = np.zeros([16 + 1], dtype=np.complex64)

for k in range(-((-len(U_list)+1)//9)):
    label_i_U = Label(
        frm_U,
        text='i'
    )

    label_i_U.grid(
        row=2*k,
        column=0,
        sticky=NSEW
    )

    label_U = Label(
        frm_U,
        text='U[i], кВ'
    )

    label_U.grid(
        row=2*k + 1,
        column=0,
        sticky=NSEW
    )

    for i in range(1, 9 + 1):
        delta = (len(U_list) - 1) - 9*k
        if delta < 9:
            for j in range(1, delta + 1):
                label_count = Label(
                    frm_U,
                    text=str(j + 9*k)
                )

                label_count.grid(
                    row=2*k,
                    column=j,
                    sticky=NSEW
                )
                
                label_U_list = Label(
                    frm_U,
                    text=str(U_list[j + 9*k])
                )

                label_U_list.grid(
                    row=2*k + 1,
                    column=j,
                    sticky=NSEW
                )

        else:
            label_count = Label(
                frm_U,
                text=str(i + 9*k)
            )

            label_count.grid(
                row=2*k,
                column=i,
                sticky=NSEW
            )
            
            label_U_list = Label(
                frm_U,
                text=str(U_list[i + 9*k])
            )

            label_U_list.grid(
                row=2*k + 1,
                column=i,
                sticky=NSEW
            )

for i in range(10):
    frm_U.columnconfigure(
        index=i,
        weight=1
    )

for i in range(4):
    frm_U.rowconfigure(
        index=i,
        weight=1
    )

### X
X_list = np.zeros([11 + 1], dtype=np.complex64)

for k in range(-((-len(X_list)+1)//9)):
    label_i_X = Label(
        frm_X,
        text='i'
    )

    label_i_X.grid(
        row=2*k,
        column=0,
        sticky=NSEW
    )

    label_X = Label(
        frm_X,
        text='X[i], кВ'
    )

    label_X.grid(
        row=2*k + 1,
        column=0,
        sticky=NSEW
    )

    for i in range(1, 9 + 1):
        delta = (len(X_list) - 1) - 9*k
        if delta < 9:
            for j in range(1, delta + 1):
                label_count = Label(
                    frm_X,
                    text=str(j + 9*k)
                )

                label_count.grid(
                    row=2*k,
                    column=j,
                    sticky=NSEW
                )
                
                label_X_list = Label(
                    frm_X,
                    text=str(X_list[j + 9*k])
                )

                label_X_list.grid(
                    row=2*k + 1,
                    column=j,
                    sticky=NSEW
                )

        else:
            label_count = Label(
                frm_X,
                text=str(i + 9*k)
            )

            label_count.grid(
                row=2*k,
                column=i,
                sticky=NSEW
            )
            
            label_X_list = Label(
                frm_X,
                text=str(X_list[i + 9*k])
            )

            label_X_list.grid(
                row=2*k + 1,
                column=i,
                sticky=NSEW
            )

for i in range(11):
    frm_X.columnconfigure(
        index=i,
        weight=1
    )

for i in range(4):
    frm_X.rowconfigure(
        index=i,
        weight=1
    )