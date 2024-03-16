from board import *


class Game:
    def __init__(self):
        self.initial_board = None
        self.num_rounds = 0

    def start(self, rounds, board):
        """Manages the Game of Life simulation for a specified number of rounds"""
        self.num_rounds = rounds
        self.initial_board = board
        print("Initial populated board: ")
        print_board(self.initial_board)
        for round in range(self.num_rounds):
            print(f"Round {round + 1}")
            board = update_board(board)
            print_board(board)
