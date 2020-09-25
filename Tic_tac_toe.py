
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
    move_row = (int(input("Please insert row number: ")) -1)
    move_column = (int(input("Please insert column number: ")) -1)
    coordinates = [move_row, move_column]
    if move_row > (number_of_rows -1) or move_column > (number_of_columns - 1):
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
    for mark in array:
        if mark == "X":
            X_count += 1
        elif mark == "O":
            O_count += 1
    return X_count == number_of_winning_marks or O_count == number_of_winning_marks


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

def board_is

def is_winner(board, number_of_columns, number_of_rows):
    for row in board:
        if horizontal_or_vertical_win(row, number_of_columns):
            return True
    for column in get_columns(board, number_of_columns):
        if horizontal_or_vertical_win(column, number_of_rows):
            return True
    return False

def game():
    number_of_rows = 3
    number_of_columns = 3
    board = create_board(number_of_rows, number_of_columns)
    players = create_players()
    while not is_winner(board, number_of_columns, number_of_rows):
         for player in players:
            print_board(board)
            coordinates = get_validated_coordinates(player, board, number_of_rows, number_of_columns)
            mark_board_with_player_move(coordinates, player, board)

game()

