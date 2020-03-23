from Errors.Exceptions import RepoError


class Repository:
    def __init__(self):
        self.__array = None
        self.__height = None
        self.__width = None
        self.__possible_moves = None
        self.__player_symbol = None
        self.__computer_symbol = None

    def set_player_symbol(self, symbol):
        """
        Function that sets the player's symbol
        :param symbol:
        :return:
        """
        self.__player_symbol = symbol

    def set_computer_symbol(self, symbol):
        """
        Function that sets the computer's symbol
        :param symbol:
        :return:
        """
        self.__computer_symbol = symbol

    def set_array(self, array):
        """
        Function that sets the array
        :param array:
        :return:
        """
        self.__array = array

    def set_height(self, value):
        """
        Function that sets the height of the array
        :param value:
        :return:
        """
        self.__height = value

    def set_width(self, value):
        """
        Function that sets the width of the array
        :param value:
        :return:
        """
        self.__width = value

    def set_possible_moves(self, possible_moves):
        """
        Function that sets the lists of possible moves
        :param possible_moves:
        :return:
        """
        self.__possible_moves = possible_moves

    def add(self, move):
        """
        Function that adds a move
        :param move:
        :return:
        """
        x = move.get_x_numerical()
        y = move.get_y()
        symbol = move.get_symbol()
        if 0 < x < self.__width and 0 < y < self.__height:
            if self.__array[y][x] == '':
                self.__array[y][x] = symbol
                self.__possible_moves[(self.__width - 1) * (y - 1) + x - 1] = 0
                if 0 < y - 1 < self.__height and 0 < x + 1 < self.__width:
                    if self.__array[y - 1][x + 1] == '':
                        self.__array[y - 1][x + 1] = '*'
                        self.__possible_moves[(self.__width - 1) * (y - 1 - 1) + x + 1 - 1] = 0
                if 0 < y < self.__height and 0 < x + 1 < self.__width:
                    if self.__array[y][x + 1] == '':
                        self.__array[y][x + 1] = '*'
                        self.__possible_moves[(self.__width - 1) * (y - 1) + x + 1 - 1] = 0
                if 0 < y + 1 < self.__height and 0 < x + 1 < self.__width:
                    if self.__array[y + 1][x + 1] == '':
                        self.__array[y + 1][x + 1] = '*'
                        self.__possible_moves[(self.__width - 1) * (y + 1 - 1) + x + 1 - 1] = 0
                if 0 < y + 1 < self.__height and 0 < x < self.__width:
                    if self.__array[y + 1][x] == '':
                        self.__array[y + 1][x] = '*'
                        self.__possible_moves[(self.__width - 1) * (y + 1 - 1) + x - 1] = 0
                if 0 < y + 1 < self.__height and 0 < x - 1 < self.__width:
                    if self.__array[y + 1][x - 1] == '':
                        self.__array[y + 1][x - 1] = '*'
                        self.__possible_moves[(self.__width - 1) * (y + 1 - 1) + x - 1 - 1] = 0
                if 0 < y < self.__height and 0 < x - 1 < self.__width:
                    if self.__array[y][x - 1] == '':
                        self.__array[y][x - 1] = '*'
                        self.__possible_moves[(self.__width - 1) * (y - 1) + x - 1 - 1] = 0
                if 0 < y - 1 < self.__height and 0 < x - 1 < self.__width:
                    if self.__array[y - 1][x - 1] == '':
                        self.__array[y - 1][x - 1] = '*'
                        self.__possible_moves[(self.__width - 1) * (y - 1 - 1) + x - 1 - 1] = 0
                if 0 < y - 1 < self.__height and 0 < x < self.__width:
                    if self.__array[y - 1][x] == '':
                        self.__array[y - 1][x] = '*'
                        self.__possible_moves[(self.__width - 1) * (y - 1 - 1) + x - 1] = 0
            else:
                raise RepoError("Invalid move!\n")
        else:
            raise RepoError("Invalid move!\n")

    def get_array(self):
        """
        Function that gets the array
        :return:
        """
        return self.__array

    def get_width(self):
        """
        Function that gets the width of the array
        :return:
        """
        return self.__width

    def get_height(self):
        """
        Function that gets the height of the array
        :return:
        """
        return self.__height

    def get_possible_moves(self):
        """
        Function that gets the list of possible moves
        :return:
        """
        return self.__possible_moves

    def get_player_symbol(self):
        """
        Function that gets the player's symbol
        :return:
        """
        return self.__player_symbol

    def get_computer_symbol(self):
        """
        Function that gets the computer's symbol
        :return:
        """
        return self.__computer_symbol
