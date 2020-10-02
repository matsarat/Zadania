import random

def create_board(number_of_rows, number_of_columns):
    board = []
    for i in range(0, number_of_rows):
        board.append(["#"] * number_of_columns)
    return board


def print_board(board):
    for row in board:
        print("  ".join(row))


def place_two_initial_elements_on_board(board, number_of_rows, number_of_columns):
    initial_element = "2"

    first_row_number = random.randint(0, number_of_rows-1)
    first_column_number = random.randint(0, number_of_columns-1)
    board[first_row_number][first_column_number] = initial_element
    print(first_row_number, first_column_number)

    second_row_number = random.randint(0, number_of_rows-1)
    second_column_number = random.randint(0, number_of_columns-1)
    while second_row_number == first_row_number and second_column_number == first_column_number:
        second_row_number = random.randint(0, number_of_rows - 1)
        second_column_number = random.randint(0, number_of_columns - 1)
        board[second_row_number][second_column_number] = initial_element
    else:
        board[second_row_number][second_column_number] = initial_element
        print(second_row_number, second_column_number)



board = create_board(4, 4)
print(place_two_initial_elements_on_board(board, 4, 4))
print_board(board)

