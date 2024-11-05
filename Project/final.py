import tkinter as tk
from customButton import CustomButton
from numpy.random.mtrand import weibull

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
graph_frame = setup_graph_frame(frame)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=2)
frame.rowconfigure(1, weight=1)

x = data.get_x_coordinates()
y = data.get_y_coordinates()

triangle = Triangle(x, y, graph_frame)
var = tk.StringVar() # https://stackoverflow.com/questions/5071559/tkinter-radio-button-initialization-bug
errorMessage = tk.StringVar()
error_label = tk.Label(frame, foreground="red", textvariable=errorMessage, wraplength=250)
error_label.grid(row=1, column=0)

def change_color(color_hex, button):
    for but in color_buttons:
        but.set_unselected_image()
    button.set_selected_image()
    triangle.change_color(color_hex)

def selection():
    selected = var.get()
    triangle.change_color(selected)

color_buttons = []
def setup_radiobutton():
    radiobutton_frame = tk.Frame(frame, highlightbackground="black", highlightthickness=1)
    radiobutton_frame.grid(row=0, column=1, sticky=tk.NW)

    global var
    var = tk.StringVar()
    var.set(data.get_first_hex())
    colors = data.get_colors()
    for i, name in enumerate(colors):
        button = CustomButton(radiobutton_frame, name)
        color_buttons.append(button)
        button.grid(row=i, column=0, sticky=tk.W)
        button.configure(command=lambda hex=colors[name], button=button: change_color(hex, button))
    color_buttons[0].set_selected_image()

def check(event):
    errorMessage.set("")
    try:
        x1 = float(x1_entry.get())
        x2 = float(x2_entry.get())
        x3 = float(x3_entry.get())
        y1 = float(y1_entry.get())
        y2 = float(y2_entry.get())
        y3 = float(y3_entry.get())
        triangle.change_coordinates((x1, x2, x3, x1), (y1, y2, y3, y1))
    except:
        errorMessage.set("Error")

def setup_entries():
    text_frame = tk.Frame(frame, width=200,  height=400, padx=10, pady=10)
    text_frame.grid(row=2, column=0, sticky=tk.W)
    text_frame.columnconfigure(0, weight=2)
    text_frame.columnconfigure(1, weight=2)
    text_frame.columnconfigure(2, weight=2)

    x_text = ["x1:", "x2:", "x3:"]
    y_text = ["y1:", "y2:", "y3:"]
    for i, name in enumerate(x_text):
        tk.Label(text_frame, text=name).grid(row=0, column=i, sticky=tk.W, padx=10)

    x1_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    x2_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    x3_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)

    x1_entry.bind('<KeyRelease>', check)
    x2_entry.bind('<KeyRelease>', check)
    x3_entry.bind('<KeyRelease>', check)

    x1_entry.insert(0, x[0])
    x2_entry.insert(0, x[1])
    x3_entry.insert(0, x[2])

    x1_entry.grid(row=1, column=0, padx=10)
    x2_entry.grid(row=1, column=1, padx=10)
    x3_entry.grid(row=1, column=2, padx=10)

    for i, name in enumerate(y_text):
        tk.Label(text_frame, text=name).grid(row=2, column=i, sticky=tk.W, padx=10)

    y1_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    y2_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    y3_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)

    y1_entry.bind('<KeyRelease>', check)
    y2_entry.bind('<KeyRelease>', check)
    y3_entry.bind('<KeyRelease>', check)

    y1_entry.insert(0, y[0])
    y2_entry.insert(0, y[1])
    y3_entry.insert(0, y[2])

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