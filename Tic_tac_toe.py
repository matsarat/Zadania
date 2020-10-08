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
    input_row = input("Please insert row number: ")
    input_column = input("Please insert column number: ")
    if input_row == "" or input_column == "":
        print("Please insert valid coordinates!")
        return get_validated_coordinates(player, board, number_of_rows, number_of_columns)
    move_row = (int(input_row) - 1)
    move_column = (int(input_column) - 1)
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


def is_current_player_winner(array, number_of_winning_marks, current_player):
    current_player_marks_count = 0
    for mark in array:
        if mark == current_player:
            current_player_marks_count += 1
            if current_player_marks_count == number_of_winning_marks:
                return True
        else:
            current_player_marks_count = 0


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


def get_all_diagonal_coordinates(number_of_rows, number_of_columns, number_of_winning_marks):
    all_diagonals = []
    for row_index in range(0, number_of_rows - (number_of_winning_marks - 1)):
        for column_index in range(0, number_of_columns - (number_of_winning_marks - 1)):
            all_diagonals.append(
                get_diagonal_coordinates(column_index, row_index, number_of_rows, number_of_columns))
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


def get_all_reverse_diagonal_coordinates(number_of_rows, number_of_columns, number_of_winning_marks):
    all_diagonals = []
    for row_index in range(0, number_of_rows - (number_of_winning_marks - 1)):
        for column_index in range(number_of_columns -1, (number_of_winning_marks - 2), -1):
            all_diagonals.append(
                get_reverse_diagonal_coordinates(column_index, row_index, number_of_rows))
    return all_diagonals


def get_all_marks_for_coordinates(board, all_coordinates):
    all_diagonal_marks = []
    for diagonals in all_coordinates:
        diagonal_marks_list = []
        for coordinate in diagonals:
            x = coordinate[0]
            y = coordinate[1]
            diagonal_marks_list.append(board[x][y])
        all_diagonal_marks.append(diagonal_marks_list)
    return all_diagonal_marks


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


def game_over(board, number_of_winning_marks, player, number_of_rows, number_of_columns):
    for row in board:
        if is_current_player_winner(row, number_of_winning_marks, player):
            return True
    for column in get_columns(board, number_of_columns):
        if is_current_player_winner(column, number_of_winning_marks, player):
            return True
    all_diagonals = get_all_diagonal_coordinates(number_of_rows, number_of_columns, number_of_winning_marks)
    all_diagonal_marks = get_all_marks_for_coordinates(board, all_diagonals)
    for diagonal in all_diagonal_marks:
        if is_current_player_winner(diagonal, number_of_winning_marks, player):
            return True
    all_reverse_diagonals = get_all_reverse_diagonal_coordinates(number_of_rows, number_of_columns, number_of_winning_marks)
    all_reverse_diagonal_marks = get_all_marks_for_coordinates(board, all_reverse_diagonals)
    for diagonal in all_reverse_diagonal_marks:
        if is_current_player_winner(diagonal, number_of_winning_marks, player):
            return True
    return False


def game(number_of_rows, number_of_columns, number_of_winning_marks):
    board = create_board(number_of_rows, number_of_columns)
    players = create_players()
    finish_game = False
    while not finish_game:
        for player in players:
            print_board(board)
            coordinates = get_validated_coordinates(player, board, number_of_rows, number_of_columns)
            mark_board_with_player_move(coordinates, player, board)
            if game_over(board, number_of_winning_marks, player, number_of_rows, number_of_columns):
                finish_game = True
                print("You won, " + str(player) + ", you lucky dick!")
                break



game(4, 4, 3)
