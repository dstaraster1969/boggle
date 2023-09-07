import english_words


class Dictionary:
    def __init__(self):
        # english_words is a dictionary that is stored in a set for cheap access.
        # I am not familiar with the vast majority of the words, but any dictionary
        # could be subbed in.
        self.dictionary = sorted(english_words.get_english_words_set(['web2'], lower=True))

    def check_for_whole_word(self, word):
        return word in self.dictionary

    def check_for_starts_with(self, word):
        for w in self.dictionary:
            if w.startswith(word):
                return True
            # if the given word isn't a prefix for the current dictionary word, check to see if
            # the loop has gone past where the word could possibly be a prefix. This keeps the loop from continuing
            # which improves perf
            if word < w:
                return False
        return False
