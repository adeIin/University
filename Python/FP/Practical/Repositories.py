from Entities import Board
import unittest


class Repository:
    def __init__(self):
        self.__array = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        self.__moves = []

    def set_array(self, array):
        self.__array = array

    def get_array(self):
        """
        Function that gets the array from repository
        :return: self.array - the array
        """
        return self.__array

    def add_move(self, move):
        if move in self.__moves:
            raise ValueError("Move already exists!\n")
        array = self.get_array()
        i = move.get_i() - 1
        j = move.get_j() - 1
        if i == -1 or j == -1:
            raise ValueError("Incorrect positions!\n")
        symbol = move.get_symbol()
        if (i > 5 or i < 0) or (j > 5 or j < 0):
            raise ValueError("Incorrect positions!\n")
        array[i][j] = symbol
        self.set_array(array)
        self.__moves.append(move)

    def get_moves(self):
        return self.__moves


class Test(unittest.TestCase):
    def test_get_array(self):
        repo = Repository()
        self.assertEqual(repo.get_array(), [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ])
