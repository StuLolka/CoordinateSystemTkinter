from data import *
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

#  https://github.com/matplotlib/matplotlib/issues/17157
class Triangle:
    __data = Data()

    def __init__(self, x, y, frame):
        self.__hex = self.__data.get_first_hex()
        self.__frame = frame
        self.__x = x
        self.__y = y
        self.__draw_triangle()

    def change_coordinates(self, x, y):
        self.__x = x
        self.__y = y
        self.__ax.clear()
        self.__draw_triangle()

    def change_color(self, hex):
        self.__hex = hex
        self.__ax.clear()
        self.__draw_triangle()

    def __draw_triangle(self):
        fig = Figure(figsize=(3, 3),
                     dpi=100)
        ax = fig.add_subplot()
        ax.plot(self.__x, self.__y)
        ax.spines['left'].set_color('red')
        ax.spines['bottom'].set_color('red')

        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.plot(self.__x, self.__y, color=self.__hex)
        ax.fill(self.__x, self.__y, color=self.__hex)

        # make arrows
        ax.plot((1), (0), ls="", marker=">", ms=10, color="red",
                transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot((0), (1), ls="", marker="^", ms=10, color="red",
                transform=ax.get_xaxis_transform(), clip_on=False)
        ax.tick_params(axis='x', colors='red')
        ax.tick_params(axis='y', colors='red')
        ax.set_xlabel('x', loc='right', color='red')
        ax.set_ylabel('y', loc='top', color='red', rotation=0)
        ax.xaxis.set_label_coords(1, 0)
        ax.set_xticks([0, 0])  # just get and reset whatever you already have
        ax.set_xticklabels([0, "(0;0)"])  # set the new/modified labels
        ax.set_yticks([])
        ax.xaxis.set_ticks_position('none')

        self.__canvas = FigureCanvasTkAgg(fig,
                                   master=self.__frame)
        self.__canvas.draw()
        self.__canvas.get_tk_widget().grid(row=0, column=0, sticky=tk.NW)
        self.__ax = ax