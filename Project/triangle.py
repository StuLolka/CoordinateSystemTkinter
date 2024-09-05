from data import *

class Triangle:
    __data = Data()

    def __init__(self, a, b, c, canvas):
        self.__hex = self.__data.get_first_hex()
        self.__canvas = canvas
        self.__a = a
        self.__b = b
        self.__c = c
        self.__setup_triangle()

    def change_coordinates(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__canvas.coords(self.__triangle, self.__a[0], self.__a[1], self.__b[0],
                                                self.__b[1], self.__c[0], self.__c[1])

    def change_color(self, hex):
        self.__hex = hex
        self.__canvas.itemconfig(self.__triangle, fill=hex)

    def __setup_triangle(self):
        self.__triangle = self.__canvas.create_polygon(self.__a[0], self.__a[1], self.__b[0],
                                                self.__b[1], self.__c[0], self.__c[1],
                                                fill=self.__hex)
        x1, y1, x2, y2 = self.__canvas.bbox(self.__triangle)
        # calculate the center (x, y) in the bounding box
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        print(f"cx = {cx}, cy = {cy}")
        # scale the polygon
        self.__canvas.scale(self.__triangle, cx, cy, 2, 2)