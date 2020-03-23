from Entities import Board, Move
import random
import unittest
from Repositories import Repository
from Validators import Validator


class Controller:
    def __init__(self, repo, valid):
        self.__repository = repo
        self.__validator = valid

    def get_board(self):
        array = self.__repository.get_array()
        board = Board(array)
        return board

    def player_move(self, i, j, symbol):
        move = Move(i, j, symbol)
        self.__repository.add_move(move)

    def get_possible_moves(self):
        array = self.__repository.get_array()
        possible_moves = []
        for i in range(6):
            for j in range(6):
                if array[i][j] == " ":
                    possible_moves.append([i + 1, j + 1])
        return possible_moves

    def computer_move(self):
        possible_moves = self.get_possible_moves()
        computer_choice = random.choice(possible_moves)
        symbols = ['x', 'o']
        computer_symbol = random.choice(symbols)
        move = Move(computer_choice[0], computer_choice[1], computer_symbol)
        self.__repository.add_move(move)

    def finish_game(self):
        array = self.__repository.get_array()
        for i in range(6):
            for j in range(6):
                if array[i][j] == " ":
                    return False
        return True

    def order_wins(self):
        """
        Function that checks if the order wins
        order wins if there are 5 symbols next to each other on the vertical diagonal or horizontal
        :return: True if order wins
                False if game continues
        """
        a = self.__repository.get_array()
        # horizontal
        for i in range(6):
            if a[i][0] == a[i][1] == a[i][2] == a[i][3] == a[i][4] != " ":
                return True
            if a[i][1] == a[i][2] == a[i][3] == a[i][4] == a[i][5] != " ":
                return True
        # vertical
        for j in range(6):
            if a[0][j] == a[1][j] == a[2][j] == a[3][j] == a[4][j] != " ":
                return True
            if a[1][j] == a[2][j] == a[3][j] == a[4][j] == a[5][j] != " ":
                return True
        # diagonal
        for i in range(2):
            if a[i][i] == a[i + 1][i + 1] == a[i + 2][i + 2] == a[i + 3][i + 3] == a[i + 4][i + 4] != " ":
                return True
        for i in range(2):
            if a[i][5 - i] == a[i + 1][4 - i] == a[i + 2][3 - i] == a[i + 3][2 - i] == a[i + 4][1 - i] != " ":
                return True
        if a[1][5] == a[2][4] == a[3][3] == a[4][2] == a[5][1] != " ":
            return True
        if a[0][4] == a[1][3] == a[2][2] == a[3][1] == a[4][0] != " ":
            return True
        if a[0][1] == a[1][2] == a[2][3] == a[3][4] == a[4][5] != " ":
            return True
        if a[1][0] == a[2][1] == a[3][2] == a[4][3] == a[5][4] != " ":
            return True
        return False

    def get_most_symbols(self):
        moves = self.__repository.get_moves()
        x = 0
        o = 0
        for move in moves:
            if move.get_symbol() == 'x':
                x += 1
            else:
                o += 1
        if x > o:
            return "x"
        else:
            return "o"

    def winning_move(self):
        a = self.__repository.get_array()
        for i in range(6):
            if a[0][i] == a[1][i] == a[2][i] == a[3][i] != " ":
                if a[4][i] == " ":
                    return [4, i, a[0][i]]
            if a[0][i] == a[1][i] == a[2][i] == a[4][i] != " ":
                if a[3][i] == " ":
                    return [3, i, a[0][i]]
            if a[0][i] == a[1][i] == a[3][i] == a[4][i] != " ":
                if a[2][i] == " ":
                    return [2, i, a[0][i]]
            if a[0][i] == a[2][i] == a[3][i] == a[4][i] != " ":
                if a[1][i] == " ":
                    return [1, i, a[0][i]]
            if a[1][i] == a[2][i] == a[3][i] == a[4][i] != " ":
                if a[0][i] == " ":
                    return [0, i, a[1][i]]
                if a[5][i] == " ":
                    return [5, i, a[1][i]]
            if a[1][i] == a[2][i] == a[3][i] == a[5][i] != " ":
                if a[4][i] == " ":
                    return [4, i, a[1][i]]
            if a[1][i] == a[2][i] == a[4][i] == a[5][i] != " ":
                if a[3][i] == " ":
                    return [3, i, a[1][i]]
            if a[2][i] == a[3][i] == a[4][i] == a[5][i] != " ":
                if a[1][i] == " ":
                    return [1, i, a[2][i]]
        for i in range(6):
            if a[i][0] == a[i][1] == a[i][2] == a[i][3] != " ":
                if a[i][4] == " ":
                    return [i, 4, a[i][0]]
            if a[i][0] == a[i][1] == a[i][2] == a[i][4] != " ":
                if a[i][3] == " ":
                    return [i, 3, a[i][0]]
            if a[i][0] == a[i][1] == a[i][3] == a[i][4] != " ":
                if a[i][2] == " ":
                    return [i, 2, a[i][0]]
            if a[i][0] == a[i][2] == a[i][3] == a[i][4] != " ":
                if a[i][1] == " ":
                    return [i, 1, a[i][0]]
            if a[i][1] == a[i][2] == a[i][3] == a[i][4] != " ":
                if a[i][0] == " ":
                    return [i, 0, a[i][1]]
                if a[i][5] == " ":
                    return [i, 5, a[i][1]]
            if a[i][1] == a[i][2] == a[i][3] == a[i][5] != " ":
                if a[i][4] == " ":
                    return [i, 4, a[i][1]]
            if a[i][1] == a[i][2] == a[i][4] == a[i][5] != " ":
                if a[i][3] == " ":
                    return [i, 3, a[i][1]]
            if a[i][2] == a[i][3] == a[i][4] == a[i][5] != " ":
                if a[i][1] == " ":
                    return [i, 1, a[i][2]]
        if a[0][0] == a[1][1] == a[2][2] == a[3][3] != " ":
            if a[4][4] == " ":
                return [4, 4, a[0][0]]
        if a[0][0] == a[1][1] == a[2][2] == a[4][4] != " ":
            if a[3][3] == " ":
                return [3, 3, a[0][0]]
        if a[0][0] == a[1][1] == a[3][3] == a[4][4] != " ":
            if a[2][2] == " ":
                return [2, 2, a[0][0]]
        if a[0][0] == a[2][2] == a[3][3] == a[4][4] != " ":
            if a[1][1] == " ":
                return [1, 1, a[0][0]]
        if a[1][1] == a[2][2] == a[3][3] == a[4][4] != " ":
            if a[0][0] == " ":
                return [0, 0, a[1][1]]
            if a[5][5] == " ":
                return [5, 5, a[1][1]]
        if a[1][1] == a[2][2] == a[3][3] == a[5][5] != " ":
            if a[4][4] == " ":
                return [4, 4, a[1][1]]
        if a[1][1] == a[2][2] == a[4][4] == a[5][5] != " ":
            if a[3][3] == " ":
                return [3, 3, a[1][1]]
        if a[2][2] == a[3][3] == a[4][4] == a[5][5] != " ":
            if a[1][1] == " ":
                return [1, 1, a[2][2]]

        if a[0][5] == a[1][4] == a[2][3] == a[3][2] != " ":
            if a[4][1] == " ":
                return [4, 1, a[0][5]]
        if a[0][5] == a[1][4] == a[2][3] == a[4][1] != " ":
            if a[3][2] == " ":
                return [3, 2, a[1][4]]
        if a[0][5] == a[1][4] == a[3][2] == a[4][1] != " ":
            if a[2][3] == " ":
                return [2, 3, a[1][4]]
        if a[0][5] == a[2][3] == a[3][2] == a[4][1] != " ":
            if a[1][4] == " ":
                return [1, 4, a[2][3]]
        if a[1][4] == a[2][3] == a[3][2] == a[4][1] != " ":
            if a[0][5] == " ":
                return [0, 5, a[1][4]]
            if a[5][0] == " ":
                return [5, 0, a[1][4]]
        if a[1][4] == a[2][3] == a[3][2] == a[5][0] != " ":
            if a[4][1] == " ":
                return [4, 1, a[1][4]]
        if a[1][4] == a[3][2] == a[4][1] == a[5][0] != " ":
            if a[2][3] == " ":
                return [2, 3, a[1][4]]
        if a[2][3] == a[3][2] == a[4][1] == a[5][0] != " ":
            if a[1][4] == " ":
                return [1, 4, a[2][3]]

        if a[1][5] == a[2][4] == a[3][3] == a[4][2] != " ":
            if a[5][1] == " ":
                return [5, 1, a[1][5]]
        if a[1][5] == a[2][4] == a[3][3] == a[5][1] != " ":
            if a[4][2] == " ":
                return [4, 2, a[1][5]]
        if a[1][5] == a[2][4] == a[4][2] == a[5][1] != " ":
            if a[2][4] == " ":
                return [2, 4, a[1][5]]
        if a[1][5] == a[3][3] == a[4][2] == a[5][1] != " ":
            if a[2][4] == " ":
                return [2, 4, a[1][5]]
        if a[2][4] == a[3][3] == a[4][2] == a[5][1] != " ":
            if a[1][5] == " ":
                return [1, 5, a[2][4]]

        if a[0][4] == a[1][3] == a[2][2] == a[3][1] != " ":
            if a[4][0] == " ":
                return [4, 0, a[0][4]]
        if a[0][4] == a[1][3] == a[2][2] == a[4][0] != " ":
            if a[3][1] == " ":
                return [3, 1, a[1][3]]
        if a[0][4] == a[1][3] == a[3][1] == a[4][0] != " ":
            if a[2][2] == " ":
                return [2, 2, a[1][3]]
        if a[0][4] == a[2][2] == a[3][1] == a[4][0] != " ":
            if a[1][3] == " ":
                return [1, 3, a[2][2]]
        if a[1][3] == a[2][2] == a[3][1] == a[4][0] != " ":
            if a[0][4] == " ":
                return [0, 4, a[1][3]]

        if a[0][1] == a[1][2] == a[2][3] == a[3][4] != " ":
            if a[4][5] == " ":
                return [4, 5, a[0][1]]
        if a[0][1] == a[1][2] == a[2][3] == a[4][5] != " ":
            if a[3][4] == " ":
                return [3, 4, a[1][2]]
        if a[0][1] == a[1][2] == a[3][4] == a[4][5] != " ":
            if a[2][3] == " ":
                return [2, 3, a[1][2]]
        if a[0][1] == a[2][3] == a[3][4] == a[4][5] != " ":
            if a[1][2] == " ":
                return [1, 2, a[2][3]]
        if a[1][2] == a[2][3] == a[3][4] == a[4][5] != " ":
            if a[0][1] == " ":
                return [0, 1, a[1][2]]

        if a[1][0] == a[2][1] == a[3][2] == a[4][3] != " ":
            if a[5][4] == " ":
                return [5, 4, a[2][1]]
        if a[1][0] == a[2][1] == a[3][2] == a[5][4] != " ":
            if a[4][3] == " ":
                return [4, 3, a[1][0]]
        if a[1][0] == a[2][1] == a[4][3] == a[5][4] != " ":
            if a[3][2] == " ":
                return [3, 2, a[4][3]]
        if a[1][0] == a[3][2] == a[4][3] == a[5][4] != " ":
            if a[2][1] == " ":
                return [2, 1, a[1][0]]
        if a[2][1] == a[3][2] == a[4][3] == a[5][4] != " ":
            if a[1][0] == " ":
                return [1, 0, a[2][1]]

        return False

    def computer_move_smart(self):
        a = self.__repository.get_array()
        winning_move = self.winning_move()
        if winning_move is not False:
            move = Move(winning_move[0] + 1, winning_move[1] + 1, winning_move[2])
            self.__repository.add_move(move)
            return
        symbol = self.get_most_symbols()
        max_neigh = 0
        position = []
        for i in range(6):
            for j in range(6):
                if a[i][j] == " ":
                    current_neighbours = 0
                    if i - 1 > 0 and j - 1 > 0:
                        if a[i - 1][j - 1] == symbol:
                            current_neighbours += 1
                    if i - 1 > 0:
                        if a[i - 1][j] == symbol:
                            current_neighbours += 1
                    if i - 1 > 0 and j + 1 < 5:
                        if a[i - 1][j + 1] == symbol:
                            current_neighbours += 1
                    if j - 1 > 0:
                        if a[i][j - 1] == symbol:
                            current_neighbours += 1
                    if j + 1 < 5:
                        if a[i][j + 1] == symbol:
                            current_neighbours += 1
                    if i + 1 < 5 and j - 1 > 0:
                        if a[i + 1][j - 1] == symbol:
                            current_neighbours += 1
                    if i + 1 < 5:
                        if a[i + 1][j] == symbol:
                            current_neighbours += 1
                    if i + 1 < 5 and j + 1 < 5:
                        if a[i + 1][j + 1] == symbol:
                            current_neighbours += 1
                    if current_neighbours > max_neigh:
                        max_neigh = current_neighbours
                        position = [i, j]
        if not position:
            self.computer_move()
            return
        move = Move(position[0] + 1, position[1] + 1, symbol)
        self.__repository.add_move(move)


class Test(unittest.TestCase):
    def test_order_wins(self):
        game_repo = Repository()
        game_valid = Validator()
        game_contr = Controller(game_repo, game_valid)
        game_contr.player_move(1, 1, 'x')
        game_contr.player_move(1, 2, 'x')
        game_contr.player_move(1, 3, 'x')
        game_contr.player_move(1, 4, 'x')
        game_contr.player_move(1, 5, 'x')
        self.assertEqual(game_contr.order_wins(), True)
        game_repo1 = Repository()
        game_valid1 = Validator()
        game_contr1 = Controller(game_repo1, game_valid1)
        game_contr1.player_move(1, 1, 'x')
        game_contr1.player_move(2, 2, 'x')
        game_contr1.player_move(3, 3, 'x')
        game_contr1.player_move(4, 4, 'x')
        game_contr1.player_move(5, 5, 'x')
        self.assertEqual(game_contr1.order_wins(), True)
        game_repo2 = Repository()
        game_valid2 = Validator()
        game_contr2 = Controller(game_repo2, game_valid2)
        game_contr2.player_move(1, 1, 'x')
        game_contr2.player_move(1, 2, 'x')
        game_contr2.player_move(1, 3, 'x')
        game_contr2.player_move(1, 4, 'x')
        game_contr2.player_move(1, 5, 'x')
        self.assertEqual(game_contr2.order_wins(), True)


