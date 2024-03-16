import copy


def create_board(size):
    """Creates the initial empty board of 8*8 .

          Returns:
          nested list : The initial empty board ."""
    board = [['-' for _ in range(size)] for _ in range(size)]
    return board


def print_board(board):
    """Prints the given game board."""
    for row in board:
        print(" ".join(map(str, row)))
    print('\n')


def number_of_neighbors(board, row, col):
    """Counts the number of a neighbors of a given cell's coordinates  in the board

    Returns: the number of a neighbors
    """
    count = 0
    for i in range(max(row - 1, 0), min(row + 1, len(board) - 1) + 1):
        for j in range(max(col - 1, 0), min(col + 1, len(board[0]) - 1) + 1):
            if (i, j) != (row, col) and board[i][j] == '#':
                count += 1
    return count


def populate_cells(board, cells):
    """Updates the game board based on the specified living cells' coordinates that we got from the user

    Returns: The populated board
    """
    for cell in cells:
        board[cell[0]][cell[1]] = '#'
    return board


def update_board(board):
    """Updates the given game board based on the rules of the Game of Life.

     Returns: The updated board"""
    updated_board = create_board((len(board)))
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbors = number_of_neighbors(board, i, j)
            # print(neighbors, i, j)
            if board[i][j] == '#':
                if neighbors < 2 or neighbors > 3:
                    updated_board[i][j] = '-'
                else:
                    updated_board[i][j] = '#'
            elif neighbors == 3:
                updated_board[i][j] = '#'

    return updated_board
