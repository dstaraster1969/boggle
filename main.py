import asyncio
import time
from board import Board


# Make main() async for concurrency
async def main():
    # Record start time so that perf can be evaluated
    start = time.time()

    board = Board()
    board.setup_board()
    print(board.board[0])
    print(board.board[1])
    print(board.board[2])
    print(board.board[3])

    await board.find_all_words()
    print(board.words)
    print(len(board.words))

    # iterations tracks how many times board.check_word() is called recursively
    print(board.iterations)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    asyncio.run(main())
