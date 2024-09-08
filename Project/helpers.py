import tkinter as tk

def setup_win(surname):
    win = tk.Tk()
    win.title(surname)
    win.geometry("650x450")
    win.eval('tk::PlaceWindow . center')
    return win

def setup_main_frame(win, change_title):
    frame = tk.Frame(win)
    frame.bind("<Button-1>", change_title)
    frame.pack(expand=1, fill="both")
    return frame

def setup_graph_frame(frame):
    graph_frame = tk.Frame(frame)
    graph_frame.grid(row=0, column=0, sticky=tk.NW, padx=5, pady=5)
    return graph_frame
