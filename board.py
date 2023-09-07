import random
from copy import deepcopy

from dice import Dice
from dictionary import Dictionary


class Board:
    def __init__(self):
        self.board = [
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
            [0 for i in range(4)],
        ]
        # Store words in a set so that the time to find a value is performant
        self.words = set()
        self.iterations = 0
        self.dict = Dictionary()

    def setup_board(self):
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

    # Using asynchronous calls allows each call to run in parallel, improving performance
    async def check_word(self, word, coordinates_visited, i, j):
        self.iterations += 1
        # i and/or j is off the board or the coordinates have been visited before
        if i < 0 or i > 3 or j < 0 or j > 3 or [i, j] in coordinates_visited:
            return
        coordinates_visited.append([i, j])
        word = (word + self.board[i][j]).lower()
        if self.dict.check_for_starts_with(word):
            # Boggle rules assert that a word needs to have at least 3 letters and no repeats
            if len(word) >= 3 and self.dict.check_for_whole_word(word) and word not in self.words:
                self.words.add(word)
                # don't return here because there could be additional words that start w/ this word
            # use deepcopy because each array needs to be uniquely tied to a call to check_word()
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
