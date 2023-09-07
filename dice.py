from random import randint


class Dice:
    # These are the 16 dice used in boggle
    dice = [
        ['A', 'A', 'E', 'E', 'G', 'N'],
        ['A', 'O', 'O', 'T', 'T', 'W'],
        ['D', 'I', 'S', 'T', 'T', 'Y'],
        ['E', 'I', 'O', 'S', 'S', 'T'],

        ['A', 'B', 'B', 'J', 'O', 'O'],
        ['C', 'I', 'M', 'O', 'T', 'U'],
        ['E', 'E', 'G', 'H', 'N', 'W'],
        ['E', 'L', 'R', 'T', 'T', 'Y'],

        ['A', 'C', 'H', 'O', 'P', 'S'],
        ['D', 'E', 'I', 'L', 'R', 'X'],
        ['E', 'E', 'I', 'N', 'S', 'U'],
        ['H', 'I', 'M', 'N', 'Q', 'U'],

        ['A', 'F', 'F', 'K', 'P', 'S'],
        ['D', 'E', 'L', 'R', 'V', 'Y'],
        ['E', 'H', 'R', 'T', 'V', 'W'],
        ['E', 'H', 'R', 'T', 'V', 'W']
    ]

    def roll_die(self, die_num):
        return self.dice[die_num][randint(0, 5)]
