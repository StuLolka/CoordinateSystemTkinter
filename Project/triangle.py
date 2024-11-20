import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Triangle:
    __fig = Figure(figsize=(2.5, 2.5))
    __ax = __fig.add_subplot()

    def __init__(self, x, y, frame, color_hex):
        self.__x = x
        self.__y = y
        self.__frame = frame
        self.__color_hex = color_hex
        self.__draw_triangle()

    def change_coordinates(self, x, y):
        self.__x = x
        self.__y = y
        self.__ax.clear()
        self.__draw_triangle()

    def change_color(self, color_hex):
        self.__color_hex = color_hex
        self.__ax.clear()
        self.__draw_triangle()

    def __create_canvas(self):
        canvas = FigureCanvasTkAgg(self.__fig,
                                   master=self.__frame)
        canvas.get_tk_widget().grid(row=0, column=0, sticky=tk.NW, padx=5, pady=5)
        canvas.draw()

    def __draw_coordinates(self):
        ax = self.__ax
        ax.set_xlim(-5, 100)
        ax.set_ylim(-5, 100)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_color('red')
        ax.spines['bottom'].set_color('red')
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2)
        ax.plot(1, 0, marker=">", color="red",
                transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, marker="^", color="red",
                transform=ax.get_xaxis_transform(), clip_on=False)
        ax.tick_params(axis='x', colors='red')
        ax.set_xticks([0], ["(0;0)"])
        ax.set_ylabel('y', loc='top', color='red', rotation=0)
        ax.set_xlabel('x', color='red', loc='right')
        ax.xaxis.set_label_coords(1, 0)
        ax.set_yticks([])
        self.__create_canvas()

    def __draw_triangle(self):
        self.__draw_coordinates()
        ax = self.__ax
        ax.plot(self.__x, self.__y, color=self.__color_hex)
        ax.fill(self.__x, self.__y, color=self.__color_hex)
        self.__create_canvas()


