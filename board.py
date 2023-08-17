from dice import Dice


class Board:
    def __init__(self):
        self.board = [
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
        ]

    def setup_board(self):
        dice_counter = 0
        for i in range(0, 4):
            for j in range(0, 4):
                self.board[i][j] = Dice().roll_die(dice_counter)
                dice_counter += 1

        print(self.board)

