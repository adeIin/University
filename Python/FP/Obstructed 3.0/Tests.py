import unittest
from Business.Services import GameService
from Infrastructure.Repositories import Repository
from Domain.Validators import Validator


class Tests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testService(self):
        gameRepo = Repository()
        gameValid = Validator()
        gameSrv = GameService(gameRepo, gameValid)
        gameSrv.set_symbols('X', 'O')
        gameSrv.set_board_size(6, 5)
        gameSrv.set_array()
        gameSrv.set_possible_moves()
        gameSrv.player_move('a', 5)
        # gameSrv.computer_move()
        gameSrv.check_game_over()
        self.assertEqual(gameSrv.get_player_symbol(), 'X')
        self.assertEqual(gameSrv.get_computer_symbol(), 'O')
        self.assertEqual(gameSrv.get_array(), [[':) ', ' a ', ' b ', ' c ', ' d ', ' e ', ' f '],
                                               ['5', 'X', '*', '', '', '', ''],
                                               ['4', '*', '*', '', '', '', ''],
                                               ['3', '', '', '', '', '', ''],
                                               ['2', '', '', '', '', '', ''],
                                               ['1', '', '', '', '', '', '']])
        self.assertEqual(gameSrv.get_possible_moves(), [0, 0, ['c', 5], ['d', 5], ['e', 5], ['f', 5], 0, 0, ['c', 4],
                                                        ['d', 4], ['e', 4], ['f', 4], ['a', 3], ['b', 3], ['c', 3],
                                                        ['d', 3], ['e', 3], ['f', 3], ['a', 2], ['b', 2], ['c', 2],
                                                        ['d', 2], ['e', 2], ['f', 2], ['a', 1], ['b', 1], ['c', 1],
                                                        ['d', 1], ['e', 1], ['f', 1]])
        self.assertEqual(gameSrv.check_game_over(), False)
