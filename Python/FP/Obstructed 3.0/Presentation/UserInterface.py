import time
from Errors.Exceptions import RepoError, UIError


class Console:
    def __init__(self, gameSrv):
        self.__game_service = gameSrv

    def __ui_print(self):
        board = self.__game_service.get_board()
        print(board)

    def __ui_player_move(self):
        move = input("Your turn now. Please make a move!(letter + number, for example: 'd4')\n>>>")
        if len(move) != 2 or move[0] not in 'abcdefgh' or move[1] not in '12345678':
            raise UIError("Invalid move!\n")
        self.__game_service.player_move(move[0], int(move[1]))

    def __ui_computer_move(self):
        print("Computer's turn. Let him think!")
        time.sleep(2)
        self.__game_service.computer_move()

    def __ui_check_game_over(self):
        return self.__game_service.check_game_over()

    def __ui_startMenu(self):
        print("\n\nObstruction game!\n"
              "Description\nThe game is played on a grid. One player is 'O' and the other is 'X'."
              "\nPlayers take turns in writing their symbol in a cell."
              "\nThe restriction is that you can only play in a cell if all its neighbours are empty."
              "\nThe first player unable to move loses.")
        cmd = input("Press any key to start or '0' to exit!\n>>>")
        if cmd == '0':
            return False
        while True:
            size_of_table = input("Insert the size of the table(6x5, 6x6, 7x6, 8x7, 8x8) or '0' to exit!:\n>>>")
            if size_of_table == '0':
                return False
            if 'x' not in size_of_table or len(size_of_table) != 3:
                print("Invalid size of table!\nPlease try again!\n")
            else:
                if size_of_table[1] == 'x':
                    parts = size_of_table.split("x")
                    try:
                        width = int(parts[0])
                        height = int(parts[1])
                        if 5 < width < 9 and 4 < height < 9:
                            self.__game_service.set_board_size(width, height)
                            self.__game_service.set_array()
                            self.__game_service.set_possible_moves()
                            break
                        else:
                            print("Invalid size of table!\nPlease try again!\n")
                    except ValueError:
                        print("Invalid size of table!\nPlease try again!\n")
                else:
                    print("Invalid size of table!\nPlease try again!\n")
        while True:
            userFirst = input("Would you like to go first?(y/n)\n>>>")
            if userFirst == 'y':
                self.__game_service.set_symbols('X', 'O')
                return True
            if userFirst == 'n':
                self.__game_service.set_symbols('O', 'X')
                return False
            print("Invalid response!\nPlease try again!\n")

    def run(self):
        if self.__ui_startMenu():
            while True:
                try:
                    self.__ui_print()
                    if self.__ui_check_game_over():
                        print("Game over!\nComputer won!")
                        return
                    self.__ui_player_move()
                    self.__ui_print()
                    if self.__ui_check_game_over():
                        print("Game over!\nYou've won!")
                        return
                    self.__ui_computer_move()
                    self.__ui_print()
                except UIError as uie:
                    print("UI error:\n" + str(uie))
                except RepoError as re:
                    print("Repo Error:\n" + str(re))
        else:
            while True:
                try:
                    self.__ui_print()
                    if self.__ui_check_game_over():
                        print("Game over!\nYou've won!")
                        return
                    self.__ui_computer_move()
                    self.__ui_print()
                    if self.__ui_check_game_over():
                        print("Game over!\nComputer won!")
                        return
                    self.__ui_player_move()
                    self.__ui_print()
                except UIError as uie:
                    print("UI error:\n" + str(uie))
                except RepoError as re:
                    print("Repo Error:\n" + str(re))
