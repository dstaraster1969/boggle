import random
from copy import deepcopy

from PyDictionary import PyDictionary

from dice import Dice
from dictionary import Dictionary


class Board:
    def __init__(self):
        self.dictionary = PyDictionary()
        self.board = [
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
        ]
        self.words = []
        self.iterations = 0
        self.dict = Dictionary()

    def setup_board(self):
        # self.board[0][0] = 'T'
        # self.board[1][0] = 'E'
        # self.board[2][0] = 'I'
        # self.board[3][0] = 'E'
        #
        # self.board[0][1] = 'S'
        # self.board[1][1] = 'A'
        # self.board[2][1] = 'N'
        # self.board[3][1] = 'H'
        #
        # self.board[0][2] = 'E'
        # self.board[1][2] = 'I'
        # self.board[2][2] = 'H'
        # self.board[3][2] = 'O'
        #
        # self.board[0][3] = 'C'
        # self.board[1][3] = 'W'
        # self.board[2][3] = 'P'
        # self.board[3][3] = 'L'
        dice = Dice()
        for i in range(0, 4):
            for j in range(0, 4):
                die = random.randint(0, len(dice.dice) - 1)
                self.board[i][j] = dice.roll_die(die)
                del dice.dice[die]

    async def find_all_words(self):
        for i in range(4):
            for j in range(4):
                await self.check_word('', [], i, j)

    async def check_word(self, word, coordinates_visited, i, j):
        self.iterations += 1
        # i and/or j is off the board or has been used before
        if i < 0 or i > 3 or j < 0 or j > 3:
            return
        if [i, j] in coordinates_visited:
            return
        coordinates_visited.append([i, j])
        word = (word + self.board[i][j]).lower()
        if self.dict.check_for_starts_with(word):
            if len(word) >= 3 and self.dict.check_for_whole_word(word):
                self.words.append(word)
                # don't return here because there could be additional words that start w/ this word
            await self.check_word(word, deepcopy(coordinates_visited), i, j - 1)
            await self.check_word(word, deepcopy(coordinates_visited), i, j + 1)
            await self.check_word(word, deepcopy(coordinates_visited), i + 1, j - 1)
            await self.check_word(word, deepcopy(coordinates_visited), i + 1, j + 1)
            await self.check_word(word, deepcopy(coordinates_visited), i + 1, j)
            await self.check_word(word, deepcopy(coordinates_visited), i - 1, j)
            await self.check_word(word, deepcopy(coordinates_visited), i - 1, j - 1)
            await self.check_word(word, deepcopy(coordinates_visited), i - 1, j + 1)
        else:
            return

    # def build_word(self, word, i, j):
    #     if 0 <= i < 4 and 0 <= j < 4:
    #         return word + self.board[i][j]
    #     return word
