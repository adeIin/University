import time


class Console:
    def __init__(self, contr):
        self.__controller = contr

    def __ui_player_move(self):
        move = input("Your turn! Insert move(ijsymbol):\n>>>")
        if len(move) != 3:
            raise ValueError("Invalid move!\n")
        i = int(move[0])
        j = int(move[1])
        symbol = move[2]
        if len(symbol) != 1 or symbol not in "xo":
            raise ValueError("Invalid move!")
        self.__controller.player_move(i, j, symbol)

    def __ui_computer_move(self):
        print("Computer's turn!\n")
        time.sleep(0.7)
        self.__controller.computer_move_smart()

    def __ui_print_board(self):
        board = self.__controller.get_board()
        print(board)

    def __ui_chaos_wins(self):
        print("Game Over!\nChaos wins!\n")

    def __ui_order_wins(self):
        print("Game Over!\nOrder wins!\n")

    def __ui_start_menu(self):
        input("Press anything to start the game!\n")

    def run(self):
        self.__ui_print_board()
        self.__ui_start_menu()
        ok = 0
        while True:
            try:
                if ok == 1:
                    self.__ui_player_move()
                    ok = 0
                else:
                    self.__ui_print_board()
                    if self.__controller.finish_game():
                        self.__ui_chaos_wins()
                        return
                    if self.__controller.order_wins():
                        self.__ui_order_wins()
                        return
                    self.__ui_computer_move()
                    self.__ui_print_board()
                    if self.__controller.finish_game():
                        self.__ui_chaos_wins()
                        return
                    if self.__controller.order_wins():
                        self.__ui_order_wins()
                        return
                    self.__ui_player_move()
            except ValueError as ve:
                print(str(ve))
                ok = 1
