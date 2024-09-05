import tkinter as tk
from data import Data
from triangle import Triangle
from helpers import *

isSurnameShowed = True
data = Data()

win = setup_win(data.get_surname())

def change_title(event):
    global isSurnameShowed
    global data
    if isSurnameShowed:
        win.title(data.get_id())
    else:
        win.title(data.get_surname())
    isSurnameShowed = not isSurnameShowed

frame = setup_main_frame(win, change_title)
canvas = setup_canvas(frame)

x1, x2, x3 = data.get_x_coordinates()
y1, y2, y3 = data.get_y_coordinates()

triangle = Triangle((x1, y1), (x2, y2), (x3,  y3), canvas)
var = tk.StringVar() # https://stackoverflow.com/questions/5071559/tkinter-radio-button-initialization-bug

def selection():
   selected = var.get()
   triangle.change_color(selected)

def setup_radiobutton():

    radiobutton_frame = tk.Frame(frame, highlightbackground="black", highlightthickness=1)
    radiobutton_frame.grid(row=0, column=2, sticky=tk.NE)

    global var
    var = tk.StringVar()
    var.set(list(data.get_colors())[0])
    colors = data.get_colors()
    for r, name in enumerate(colors):
        tk.Radiobutton(radiobutton_frame, text=name, variable=var, value=colors[name], padx=10, pady=5, command=selection) \
            .grid(row=r + 1, column=1, sticky=tk.W)

def check(event):
    triangle.change_coordinates((x1_entry.get(), y1_entry.get()), (x2_entry.get(), y2_entry.get()), (x3_entry.get(), y3_entry.get()))

def setup_entries():
    text_frame = tk.Frame(frame, width=200,  height=400)
    text_frame.grid(row=1, column=0, sticky=tk.W)

    x = ["x1:", "x2:", "x3:"]
    y = ["y1:", "y2:", "y3:"]
    for i, name in enumerate(x):
        tk.Label(text_frame, text=name).grid(row=0, column=i, sticky=tk.W, padx=10)

    x1_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    x2_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    x3_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)

    x1_entry.bind('<KeyRelease>', check)
    x2_entry.bind('<KeyRelease>', check)
    x3_entry.bind('<KeyRelease>', check)

    x1_entry.insert(0, x1)
    x2_entry.insert(0, x2)
    x3_entry.insert(0, x3)

    x1_entry.grid(row=1, column=0, padx=10)
    x2_entry.grid(row=1, column=1, padx=10)
    x3_entry.grid(row=1, column=2, padx=10)

    for i, name in enumerate(y):
        tk.Label(text_frame, text=name).grid(row=2, column=i, sticky=tk.W, padx=10)

    y1_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    y2_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    y3_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)

    y1_entry.bind('<KeyRelease>', check)
    y2_entry.bind('<KeyRelease>', check)
    y3_entry.bind('<KeyRelease>', check)

    y1_entry.insert(0, y1)
    y2_entry.insert(0, y2)
    y3_entry.insert(0, y3)

    y1_entry.grid(row=3, column=0, padx=10)
    y2_entry.grid(row=3, column=1, padx=10)
    y3_entry.grid(row=3, column=2, padx=10)
    return (x1_entry,
             x2_entry,
             x3_entry,
             y1_entry,
            y2_entry,
            y3_entry)




setup_radiobutton()
x1_entry, x2_entry, x3_entry, y1_entry, y2_entry, y3_entry = setup_entries()

win.mainloop()