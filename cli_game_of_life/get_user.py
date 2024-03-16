import logging


def get_user_rounds():
    """Asks the user to enter the number of rounds.

       Returns:
       int: The number of rounds entered by the user.

       Raises:
       ValueError: If the user input is not a valid integer."""
    while True:
        try:
            number_rounds = int(input("Enter the number of rounds to simulate: "))
            break
        except ValueError as e:
            logging.error(f"Input error: {e}")
            print(f"Invalid input: {e}")

    return number_rounds


def get_user_cell(board, cells_list):
    """Asks the user to enter the coordinates of a cell he wants to populate.

          Returns:
          int: The coordinates of the cell

          Raises:
          ValueError: If the user input is not a valid integer.
          Warning : If the coordinates is for a cell that already populated

          """

    while True:
        try:
            x = int(input("Enter the x-coordinate of the living square (1-8): ")) - 1
            y = int(input("Enter the y-coordinate of the living square (1-8): ")) - 1
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                if [x, y] in cells_list:
                    raise UserWarning("This cell is already populated,choose another cell")
                else:
                    return [x, y]
            else:
                raise ValueError("Invalid coordinates. Please enter values between 1 and 8.")

        except ValueError as e:
            logging.error(f"Input error: {e}")
            print(f"Error: {e}")
        except UserWarning as e:
            logging.warning(f"Input warning: {e.args[0]}")
            print(f"Warning: {e.args[0]}")


def ask_for_more_cells(board):
    """Asks the user if he wants to enter more cells.

          Returns:
          list : A List of all the coordinates of the cells he wants to populate

          Raises:
          ValueError: If the user input is not yes or no word.
          """
    cells_list = []
    while True:
        try:
            add_more = input("Do you want to add more living squares? (yes/no): ")
            while add_more.lower() == 'yes':
                cells_list.append(get_user_cell(board, cells_list))
                add_more = input("Do you want to add more living squares? (yes/no): ")
            if add_more.lower() == 'no':
                break
            else:
                raise ValueError("Invalid input,please enter yes or no:")

        except ValueError as e:
            logging.error(f"Input error: {e}")
            print(f"Error: {e}")

    return cells_list
