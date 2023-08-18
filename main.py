from board import Board


def main():
    board = Board()
    board.setup_board()
    print(board.board[0])
    print(board.board[1])
    print(board.board[2])
    print(board.board[3])

    board.generate_list_of_words('', 0, 0, [])
    print(board.words)

if __name__ == '__main__':
    main()