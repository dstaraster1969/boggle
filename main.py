import asyncio
import time

from board import Board


async def main():
    start = time.time()
    board = Board()
    board.setup_board()

    # Print out the randomly generated board
    print(board.board[0])
    print(board.board[1])
    print(board.board[2])
    print(board.board[3])

    # Wait for all the calls return
    await board.find_all_words()
    print(f'List of words found: {board.words}')
    end = time.time()

    # Display the amount of time it took to run to demonstrate that it doesn't take more than 3 minutes
    print(f'Time to completion: {end - start}')


if __name__ == '__main__':
    asyncio.run(main())
