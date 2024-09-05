import tkinter as tk

def setup_win(surname):
    win = tk.Tk()
    win.title(surname)
    win.geometry("500x500")
    win.eval('tk::PlaceWindow . center')
    return win

def setup_main_frame(win, change_title):
    frame = tk.Frame(win)
    frame.bind("<Button-1>", change_title)
    frame.pack(expand=1, fill="both")
    return frame

def setup_canvas(frame):
    canvas = tk.Canvas(frame, width=250, height=200)
    canvas.grid(row=0, column=0, sticky=tk.NW)
    return canvas
