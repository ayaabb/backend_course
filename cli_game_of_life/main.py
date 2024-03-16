from get_user import *
from Game import *

life_game = Game()
num_of_rounds = get_user_rounds()
board = create_board(8)
print_board(board)
# cells = ask_for_more_cells(board)
# cells = [[0, 0], [0, 1], [1, 1], [0, 2], [1, 3], [2, 1], [3, 1], [3, 0], [3, 2]]
cells = [
    (2, 3), (2, 4), (2, 5),
    (3, 3), (3, 4), (3, 5),
    (4, 3), (4, 4), (4, 5),
]
board = populate_cells(board, cells)
life_game.start(num_of_rounds, board)
