from Project.triangle import Triangle
from data import Data
from setupUI import *

data = Data()
win = setup_win(data.get_surname())

isSurnameShowed = True
def change_title(event):
    global isSurnameShowed
    win.title(data.get_id()) if isSurnameShowed else win.title(data.get_surname())
    isSurnameShowed = not isSurnameShowed

frame = setup_main_frame(win, change_title)

x = data.get_x_coordinates()
y = data.get_y_coordinates()
triangle = Triangle(data.get_x_coordinates(), data.get_y_coordinates(), frame, data.get_first_hex())

error_message = tk.StringVar()
setup_error_label(frame, error_message)

def check_coordinates(event):
    error_message.set("")
    try:
        x1 = float(x1_entry.get())
        x2 = float(x2_entry.get())
        x3 = float(x3_entry.get())
        y1 = float(y1_entry.get())
        y2 = float(y2_entry.get())
        y3 = float(y3_entry.get())
        triangle.change_coordinates((x1, x2, x3, x1), (y1, y2, y3, y1))
    except:
        error_message.set("Ошибка! Некорректный ввод.")
    event.widget.focus_force()

x1_entry, x2_entry, x3_entry, y1_entry, y2_entry, y3_entry = setup_entries(frame, check_coordinates, x, y)

def change_color(color_hex, button):
    for but in color_buttons:
        but.set_unselected_image()
    button.set_selected_image()
    triangle.change_color(color_hex)

color_buttons = setup_color_buttons(frame, data.get_colors(), change_color)
win.mainloop()