import time

import english_words


class Dictionary:
    def __init__(self):
        start = time.time()
        self.dictionary = sorted(english_words.get_english_words_set(['web2'], lower=True))
        end = time.time()
        print(f'time to sort: {end - start}')

    def check_for_whole_word(self, word):
        return word in self.dictionary

    def check_for_starts_with(self, word):
        for w in self.dictionary:
            if w.startswith(word):
                return True
            if word < w:
                return False
        return False
