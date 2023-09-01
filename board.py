import random
from copy import deepcopy
from PyDictionary import PyDictionary
from dice import Dice
from dictionary import Dictionary


class Board:
    def __init__(self):
        # Initialize 4x4 board with 0 as placeholder
        self.board = [
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
        ]

        # Array to hold the words that are found in the dictionary
        self.words = []

        # Iterations keeps track of the number of times check_word() is called recursively
        self.iterations = 0
        self.dict = Dictionary()

    # Randomly assign dice to each position on the board, without replacement
    def setup_board(self):
        dice = Dice()
        for i in range(0, 4):
            for j in range(0, 4):
                die = random.randint(0, len(dice.dice) - 1)
                self.board[i][j] = dice.roll_die(die)
                del dice.dice[die]

    # Get everything started
    async def find_all_words(self):
        for i in range(4):
            for j in range(4):
                await self.check_word('', [], i, j)

    # The heart of the app. Called recursively to find all valid words on the board
    async def check_word(self, word, coordinates_visited, i, j):
        self.iterations += 1

        # i and/or j is off the board or has been used before
        if i < 0 or i > 3 or j < 0 or j > 3 or [i, j] in coordinates_visited:
            return

        # The same letter can't be used more than once in a word, so keep track of the letters
        # that have already been used for each attempted word
        coordinates_visited.append([i, j])

        # By making the words all lowercase, proper nouns in the dictionary are avoided
        word = (word + self.board[i][j]).lower()

        # See if at this point the word is a prefix for any words
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
