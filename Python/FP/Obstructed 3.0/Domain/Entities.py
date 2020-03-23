from texttable import Texttable


class Move(object):
    def __init__(self, x, y, symbol):
        self.__x = x
        self.__y = y
        self.__symbol = symbol

    def get_x(self):
        """
        Function that gets the x of the move
        :return:
        """
        return self.__x

    def get_x_numerical(self):
        """
        Function that gets the numerical x of the move
        :return:
        """
        x = None
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(len(letters)):
            if letters[i] == self.__x:
                x = i + 1
        return x

    def get_y(self):
        """
        Function that gets the y of the move
        :return:
        """
        return self.__y

    def get_symbol(self):
        """
        Function that gets the symbol of the move
        :return:
        """
        return self.__symbol


class Board(object):

    def __init__(self, rowsArray):
        self.__table = Texttable()
        self.__rows_array = rowsArray
        self.__table.add_rows(rowsArray, header=False)

    def get_rows_array(self):
        """
        Function that gets the rows array for the board
        :return:
        """
        return self.__rows_array

    def __str__(self):
        """
        Function that makes the board a string
        :return:
        """
        return self.__table.draw() + "\n"
