from texttable import Texttable


class Board:
    def __init__(self, rows_array):
        self.__rows_array = rows_array
        self.__table = Texttable()
        self.__table.add_rows(rows_array, header=False)

    def __str__(self):
        return self.__table.draw() + "\n"


class Move:
    def __init__(self, i, j, symbol):
        self.__i = i
        self.__j = j
        self.__symbol = symbol

    def get_i(self):
        return self.__i

    def get_j(self):
        return self.__j

    def get_symbol(self):
        return self.__symbol

    def __eq__(self, other):
        return self.__i == other.__i and self.__j == other.__j
