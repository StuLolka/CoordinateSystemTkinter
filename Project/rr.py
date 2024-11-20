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

win.mainloop()