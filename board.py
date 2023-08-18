from PyDictionary import PyDictionary

from dice import Dice


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

    def setup_board(self):
        dice_counter = 0
        for i in range(0, 4):
            for j in range(0, 4):
                self.board[i][j] = Dice().roll_die(dice_counter)
                dice_counter += 1

    def generate_list_of_words(self, word, i, j, coordinates_visited):
        word, finished = self.build_word(word, i, j)
        coordinates_visited.append([i, j])
        if len(word) >=3 and self.check_dictionary_for_word(word):
            self.words.append(word)
        if not finished:
            if not [i-1, j-1] in coordinates_visited:
                self.generate_list_of_words(word, i-1, j-1, coordinates_visited)
            if not [i-1, j] in coordinates_visited:
                self.generate_list_of_words(word, i-1, j, coordinates_visited)
            if not [i-1, j+1] in coordinates_visited:
                self.generate_list_of_words(word, i-1, j+1, coordinates_visited)
            if not [i, j-1] in coordinates_visited:
                self.generate_list_of_words(word, i, j-1, coordinates_visited)
            if not [i, j+1] in coordinates_visited:
                self.generate_list_of_words(word, i, j+1, coordinates_visited)
            if not [i+1, j-1] in coordinates_visited:
                self.generate_list_of_words(word, i+1, j-1, coordinates_visited)
            if not [i+1, j] in coordinates_visited:
                self.generate_list_of_words(word, i+1, j, coordinates_visited)
            if not [i+1, j+1] in coordinates_visited:
                self.generate_list_of_words(word, i+1, j+1, coordinates_visited)

    def check_dictionary_for_word(self, word):
        try:
            meaning = self.dictionary.meaning(word, disable_errors=True)
            if meaning:
                return True
            return False
        except IndexError as e:
            pass

    def build_word(self, word, i, j):
        if 0 <= i < 4 and 0 <= j < 4:
            return word + self.board[i][j], False
        return word, True
