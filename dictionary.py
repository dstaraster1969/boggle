import english_words


class Dictionary:
    def __init__(self):
        self.dictionary = english_words.get_english_words_set(['web2'], lower=True)

    def check_for_whole_word(self, word):
        return word in self.dictionary

    def check_for_starts_with(self, word):
        for w in self.dictionary:
            if w.startswith(word):
                return True
        return False
