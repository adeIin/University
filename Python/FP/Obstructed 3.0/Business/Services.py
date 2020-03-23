from Domain.Entities import Board, Move
import random


class GameService:
    def __init__(self, gameRepository, gameValidator):
        self.__repository = gameRepository
        self.__validator = gameValidator

    def set_symbols(self, player_symbol, computer_symbol):
        """
        Function that sets the player's and the computer's symbols
        :param player_symbol:
        :param computer_symbol:
        :return:
        """
        self.__repository.set_player_symbol(player_symbol)
        self.__repository.set_computer_symbol(computer_symbol)

    def set_board_size(self, width, height):
        """
        Function that sets the board size
        :param width:
        :param height:
        :return:
        """
        self.__repository.set_width(width + 1)
        self.__repository.set_height(height + 1)

    def set_array(self):
        """
        Function that sets the empty board
        :return:
        """
        width = self.__repository.get_width()
        height = self.__repository.get_height()
        array = []
        letters = [':) ', ' a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', ' h ']
        row = []
        for i in range(width):
            row.append(letters[i])
        array.append(row)
        for i in range(height - 1, 0, -1):
            row = [str(i)]
            for j in range(width - 1):
                row.append('')
            array.append(row)
        self.__repository.set_array(array)

    def set_possible_moves(self):
        """
        Function that sets the list of possible moves
        :return:
        """
        width = self.__repository.get_width()
        height = self.__repository.get_height()
        possible_moves = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(height - 1, 0, -1):
            for j in range(1, width, 1):
                mini_move = [letters[j - 1], i]
                possible_moves.append(mini_move)
        self.__repository.set_possible_moves(possible_moves)

    def get_array(self):
        """
        Function that gets the array for the board
        :return:
        """
        return self.__repository.get_array()

    def get_board(self):
        """
        Function that gets the board
        :return:
        """
        array = self.get_array()
        board = Board(array)
        return board

    def get_possible_moves(self):
        """
        Function that gets the list of possible moves
        :return:
        """
        return self.__repository.get_possible_moves()

    def get_player_symbol(self):
        """
        Function that gets the player's symbol
        :return:
        """
        return self.__repository.get_player_symbol()

    def get_computer_symbol(self):
        """
        Function that gets the computer's symbol
        :return:
        """
        return self.__repository.get_computer_symbol()

    def add_move(self, letter, number, symbol):
        """
        Function that adds a move
        :param letter:
        :param number:
        :param symbol:
        :return:
        """
        height = self.__repository.get_height()
        y = height - number
        move = Move(letter, y, symbol)
        self.__repository.add(move)

    def player_move(self, letter, number):
        """
        Function that create a move for the player and adds it
        :param letter:
        :param number:
        :return:
        """
        player_symbol = self.__repository.get_player_symbol()
        self.add_move(letter, number, player_symbol)

    def computer_move(self):
        """
        Function that create a move for the computer and adds it
        :return:
        """
        computer_symbol = self.get_computer_symbol()
        possible_moves = self.get_possible_moves()
        available_moves = []
        for i in range(len(possible_moves)):
            if possible_moves[i] != 0:
                available_moves.append(possible_moves[i])
        if not available_moves:
            raise ValueError("Computer out of moves\n")
        computer_choice = random.choice(available_moves)
        self.add_move(computer_choice[0], computer_choice[1], computer_symbol)

    def check_game_over(self):
        """
        Function that checks if the game is over
        :return:
        """
        possible_moves = self.get_possible_moves()
        for i in range(len(possible_moves)):
            if possible_moves[i] != 0:
                return False
        return True


