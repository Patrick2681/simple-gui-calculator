from tkinter import *
import re, os, sys

root = Tk()
root.title("Simple Calculator")
root.geometry("283x333")
root.resizable(0, 0)

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


win_icon = resource_path("favicon.ico")
lix_icon = resource_path("@favicon.xbm")
try: root.wm_iconbitmap(win_icon)
except: root.iconbitmap(lix_icon)


entry = Entry(root, borderwidth=2, font=('Times New Roman', 20, 'bold'), background='#3A3535', fg='white')
entry.grid(row=0, column=0, columnspan=4, rowspan=1, ipady=13, ipadx=7)


def remove_letter(event):
    if re.search('[a-zA-Z]', entry.get()):
        operation = re.sub(r'[a-zA-Z]+', '', entry.get())
        entry.delete(0, END)
        entry.insert(0, operation)


def clear():
    entry.delete(0, END)


def number_add(number):
    if '=' not in entry.get(): number = entry.get() + str(number)
    entry.delete(0, END)
    entry.insert(0, number)


def operator_add(operator):
    operation = entry.get() + operator
    entry.delete(0, END)
    entry.insert(0, operation)


def calc():
    operation = entry.get()
    entry.delete(0, END)
    result = operation + ' = ' + str(eval(operation))
    entry.insert(0, result)


# BUTTONS
# FUNC BUTTONS
button_clear = Button(root, text="C", padx=57, pady=15, command=clear, borderwidth=2, background='#EAEAE4', font=('Times New Roman', 12, 'bold'))
button_divison = Button(root, text="/", padx=27, pady=15, command=lambda: operator_add('/'), borderwidth=2, background='#727070', fg='white')
button_mult = Button(root, text="X", padx=25, pady=15, command=lambda: operator_add('*'), borderwidth=2, background='#727070', fg='white')
button_add = Button(root, text="+", padx=24, pady=15, command=lambda: operator_add('+'), borderwidth=2, background='#727070', fg='white')
button_sub = Button(root, text="-", padx=27, pady=15, command=lambda: operator_add('-'), borderwidth=2, background='#727070', fg='white')
button_equals = Button(root, text="=", padx=25, pady=15, command=calc, borderwidth=2, background='#FF7F00', fg='white')

button_clear.grid(row=1, column=0, columnspan=3, sticky=NSEW)
button_divison.grid(row=1, column=3, sticky=NSEW)
button_mult.grid(row=2, column=3, sticky=NSEW)
button_add.grid(row=3, column=3, sticky=NSEW)
button_sub.grid(row=4, column=3, sticky=NSEW)
button_equals.grid(row=5, column=3, sticky=NSEW)

# NUMBER BUTTONS
button_7 = Button(root, text="7", padx=25, pady=15, command=lambda: number_add(7), borderwidth=2, background='#EAEAE4')
button_8 = Button(root, text="8", padx=25, pady=15, command=lambda: number_add(8), borderwidth=2, background='#EAEAE4')
button_9 = Button(root, text="9", padx=25, pady=15, command=lambda: number_add(9), borderwidth=2, background='#EAEAE4')

button_4 = Button(root, text="4", padx=25, pady=15, command=lambda: number_add(4), borderwidth=2, background='#EAEAE4')
button_5 = Button(root, text="5", padx=25, pady=15, command=lambda: number_add(5), borderwidth=2, background='#EAEAE4')
button_6 = Button(root, text="6", padx=25, pady=15, command=lambda: number_add(6), borderwidth=2, background='#EAEAE4')

button_1 = Button(root, text="1", padx=25, pady=15, command=lambda: number_add(1), borderwidth=2, background='#EAEAE4')
button_2 = Button(root, text="2", padx=25, pady=15, command=lambda: number_add(2), borderwidth=2, background='#EAEAE4')
button_3 = Button(root, text="3", padx=25, pady=15, command=lambda: number_add(3), borderwidth=2, background='#EAEAE4')

button_0 = Button(root, text="0", padx=57, pady=15, command=lambda: number_add(0), borderwidth=2, background='#EAEAE4')
button_dot = Button(root, text=".", padx=27, pady=15, command=lambda: number_add('.'), borderwidth=2, background='#EAEAE4')

button_7.grid(row=2, column=0, sticky=NSEW)
button_8.grid(row=2, column=1, sticky=NSEW)
button_9.grid(row=2, column=2, sticky=NSEW)

button_4.grid(row=3, column=0, sticky=NSEW)
button_5.grid(row=3, column=1, sticky=NSEW)
button_6.grid(row=3, column=2, sticky=NSEW)

button_1.grid(row=4, column=0, sticky=NSEW)
button_2.grid(row=4, column=1, sticky=NSEW)
button_3.grid(row=4, column=2, sticky=NSEW)

button_0.grid(row=5, column=0, columnspan=2, sticky=NSEW)
button_dot.grid(row=5, column=2, sticky=NSEW)

root.bind('<Key>', remove_letter)

if __name__ == "__main__":
    root.mainloop()
