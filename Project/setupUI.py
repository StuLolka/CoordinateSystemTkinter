import tkinter as tk
from customButton import CustomButton

def setup_win(window_title):
    win = tk.Tk()
    win.title(window_title)
    width = 500
    height = 380
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int(screen_width/2 - width/2)
    y = int(screen_height/2 - height/2)
    win.geometry(f"{width}x{height}+{x}+{y}")
    return win

def setup_main_frame(win, change_title):
    frame = tk.Frame(win)
    frame.pack(expand=True, fill='both')
    frame.bind("<Button-1>", change_title)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    return frame

def setup_color_buttons(frame, colors, change_color):
    if not len(colors): return
    color_buttons_frame = tk.Frame(frame, highlightbackground="black", highlightthickness=1)
    color_buttons_frame.grid(row=0, column=1, sticky=tk.NW, pady=5, ipadx=5)
    color_buttons_frame.columnconfigure(0, weight=1)

    color_buttons = []
    for index, name in enumerate(colors):
        custom_button = CustomButton(color_buttons_frame, name)
        color_buttons.append(custom_button)
        custom_button.grid(row=index, column=0, sticky=tk.W)
        custom_button.configure(command=lambda color=colors[name], button=custom_button: change_color(color, button))
        color_buttons_frame.rowconfigure(index, weight=1)
    color_buttons[0].set_selected_image()
    return color_buttons

def setup_error_label(frame, error_message):
    error_label = tk.Label(frame, foreground="red", textvariable=error_message)
    error_label.grid(row=1, column=0)

def setup_entries(frame, check, x, y):
    text_frame = tk.Frame(frame, padx=5, pady=5)
    text_frame.grid(row=2, column=0, sticky=tk.W)
    for column in range(0, 3):
        text_frame.columnconfigure(column, weight=1)
    for row in range(0, 4):
        text_frame.rowconfigure(row, weight=1)

    for column, name in enumerate(("x1:", "x2:", "x3:")):
        tk.Label(text_frame, text=name).grid(row=0, column=column, sticky=tk.W, padx=10)

    x1_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    x2_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    x3_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)

    for index, entry in enumerate((x1_entry, x2_entry, x3_entry)):
        entry.bind('<KeyRelease>', check)
        entry.insert(0, x[index])
        entry.grid(row=1, column=index, padx=10)

    for column, name in enumerate(("y1:", "y2:", "y3:")):
        tk.Label(text_frame, text=name).grid(row=2, column=column, sticky=tk.W, padx=10)

    y1_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    y2_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)
    y3_entry = tk.Entry(text_frame, width=10, highlightbackground="black", highlightthickness=1)

    for index, entry in enumerate((y1_entry, y2_entry, y3_entry)):
        entry.bind('<KeyRelease>', check)
        entry.insert(0, y[index])
        entry.grid(row=3, column=index, padx=10)

    return (x1_entry, x2_entry, x3_entry,
            y1_entry, y2_entry, y3_entry)
