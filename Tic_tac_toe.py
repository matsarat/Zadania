def create_board(number_of_rows, number_of_columns):
    board = []
    for i in range(0, number_of_rows):
        board.append(["#"] * number_of_columns)
    return board


def print_board(board):
    for row in board:
        print("  ".join(row))


def create_players():
    return ['O', 'X']


def get_validated_coordinates(player, board, number_of_rows, number_of_columns):
    print("Now plays: " + player)
    move_row = (int(input("Please insert row number: ")) - 1)
    move_column = (int(input("Please insert column number: ")) - 1)
    coordinates = [move_row, move_column]
    if move_row > (number_of_rows - 1) or move_column > (number_of_columns - 1):
        print("Your move is out of board!")
        return get_validated_coordinates(player, board, number_of_rows, number_of_columns)
    elif board[move_row][move_column] == "X" or board[move_row][move_column] == "O":
        print("The field is already taken!")
        return get_validated_coordinates(player, board, number_of_rows, number_of_columns)
    return coordinates


def mark_board_with_player_move(coordinates, player, board):
    board[coordinates[0]][coordinates[1]] = player


def horizontal_or_vertical_win(array, number_of_winning_marks):
    X_count = 0
    O_count = 0
    if X_count < number_of_winning_marks or O_count < number_of_winning_marks:
        for mark in array:
            if mark == "X":
                X_count += 1
            elif mark == "O":
                O_count += 1
            else:
                O_count = 0
                X_count = 0
    return X_count == number_of_winning_marks or O_count == number_of_winning_marks


def diagonal_win(number_of_winning_marks, board):
    for list_of_diagonals in get_all_reverse_diagonal_coordinates(number_of_rows, number_of_columns):
        for diagonal in list_of_diagonals:
            X_count = 0
            O_count = 0
            for coordinate in diagonal:
                mark = board[coordinate[0]][coordinate[1]]
                if X_count < number_of_winning_marks or O_count < number_of_winning_marks:
                    if mark == "X":
                        X_count += 1
                    elif mark == "O":
                        O_count += 1
                    else:
                        X_count = 0
                        O_count = 0
    return X_count == number_of_winning_marks or O_count == number_of_winning_marks


def reverse_diagonal_win(number_of_winning_marks, board):
    for list_of_reverse_diagonals in get_all_reverse_diagonal_coordinates(number_of_rows, number_of_columns):
        for reverse_diagonal in list_of_reverse_diagonals:
            X_count = 0
            O_count = 0
            for coordinate in reverse_diagonal:
                mark = board[coordinate[0][coordinate[1]]]
                if X_count < number_of_winning_marks or O_count < number_of_winning_marks:
                    if mark == "X":
                        X_count += 1
                    elif mark == "O":
                        O_count += 1
                    else:
                        X_count = 0
                        O_count = 0
    return X_count == number_of_winning_marks or O_count == number_of_winning_marks


def get_all_diagonal_coordinates(number_of_rows, number_of_columns):
    all_diagonals = []
    for row_index in range(0, number_of_rows-2):
        for column_index in range(0, number_of_columns-2):
            all_diagonals.append(
                get_diagonal_coordinates(column_index, row_index, number_of_rows, number_of_columns))
    return all_diagonals


def get_diagonal_coordinates(first_column_number, first_row_number, number_of_rows, number_of_columns):
    diagonal_coordinates = []
    current_column_number = first_column_number
    current_row_number = first_row_number
    while current_row_number < number_of_rows and current_column_number < number_of_columns:
        coordinate = []
        coordinate.append(current_row_number)
        coordinate.append(current_column_number)
        diagonal_coordinates.append(coordinate)
        current_column_number += 1
        current_row_number += 1
    return diagonal_coordinates


def get_all_reverse_diagonal_coordinates(number_of_rows, number_of_columns):
    all_diagonals = []
    for row_index in range(0, number_of_rows-2):
        for column_index in range(number_of_columns-1, -1+2, -1):
            all_diagonals.append(
                get_reverse_diagonal_coordinates(column_index, row_index, number_of_rows))
    return all_diagonals


def get_reverse_diagonal_coordinates(last_column_number, first_row_number, number_of_rows):
    diagonal_coordinates = []
    current_column_number = last_column_number
    current_row_number = first_row_number
    while current_row_number < number_of_rows and current_column_number >= 0:
        coordinate = []
        coordinate.append(current_row_number)
        coordinate.append(current_column_number)
        diagonal_coordinates.append(coordinate)
        current_column_number -= 1
        current_row_number += 1
    return diagonal_coordinates


def get_column(board, column_number):
    column = []
    for row in board:
        column.append(row[column_number])
    return column


def get_columns(board, number_of_columns):
    columns = []
    for column_number in range(0, number_of_columns):
        columns.append(get_column(board, column_number))
    return columns


def is_winner(board, number_of_winning_marks):
    for row in board:
        if horizontal_or_vertical_win(row, number_of_winning_marks):
            return True
    for column in get_columns(board, number_of_columns):
        if horizontal_or_vertical_win(column, number_of_winning_marks):
            return True
    if diagonal_win(number_of_winning_marks, board):
        return True
    if reverse_diagonal_win(number_of_winning_marks, board):
        return True

    return False


def game():

    board = create_board(number_of_rows, number_of_columns)
    players = create_players()
    while not is_winner(board, number_of_winning_marks):
        for player in players:
            print_board(board)
            coordinates = get_validated_coordinates(player, board, number_of_rows, number_of_columns)
            mark_board_with_player_move(coordinates, player, board)

number_of_rows = 4
number_of_columns = 4
number_of_winning_marks = 3

game()
#board = create_board(number_of_rows, number_of_columns)
# get_diagonal_coordinates(board, 0, 0, number_of_rows)
#print(get_all_diagonal_coordinates(number_of_rows, number_of_columns))
# get_diagonal_coordinates(2, 2, 10, 10)

#print(get_reverse_diagonal_coordinates(3, 0, 15))
print(get_all_reverse_diagonal_coordinates(number_of_rows, number_of_columns))
