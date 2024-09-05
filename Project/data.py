from enum import Enum

class Data:
    __surname = "Герасимова"
    __id = "70214517"

    __colors = {"Фиолетовый": "#6900C6",
                "Зеленый": "#013220",
                "Светло-голубой": "#ADD8E6",
                "Пурпурный": "#800080",
                "Охра": "#cc7722",
                "Лиловый": "#FF00FF"}

    def get_surname(self):
        return self.__surname

    def get_id(self):
        return self.__id

    def get_first_hex(self):
        return list(self.__colors.values())[0]

    def get_colors(self):
        return self.__colors

    def get_hex(self, name):
        return self.__colors[name]

    def get_x_coordinates(self):
        x1 = int(self.__id[2:4])
        x2 = int(self.__id[4:6])
        x3 = int(self.__id[6:8])
        return (x1, x2, x3)

    def get_y_coordinates(self):
        number = str(int(self.__id) // 3)
        y1 = int(number[2:4])
        y2 = int(number[4:6])
        y3 = int(number[6:8])
        return (y1, y2, y3)