import time

import english_words
from PyDictionary import PyDictionary

from board import Board
from dictionary import Dictionary


def main():
    start = time.time()
    board = Board()
    board.setup_board()
    print(board.board[0])
    print(board.board[1])
    print(board.board[2])
    print(board.board[3])
    board.find_all_words()
    print(board.words)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()