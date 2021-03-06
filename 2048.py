import random

class Field(object):
    def __init__(self):
        self.value = 0
    def __str__(self):
        return str(self.value)


def create_board(number_of_rows, number_of_columns):
    board = []
    for i in range(0, number_of_rows):
        row = []
        for j in range(0, number_of_columns):
            row.append(Field())
        board.append(row)
    return board


def print_board(board):
    for row in board:
        print("  ".join(str(field) for field in row))


def get_number_of_rows(board):
    return len(board)

def get_number_of_columns(board):
    return len(board[0])
        
def get_column(board, column_number):
    column = []
    for row in board:
        column.append(row[column_number])
    return column


def get_columns(board):
    columns = []
    for column_number in range(0, get_number_of_columns(board)):
        columns.append(get_column(board, column_number))
    return columns


def instructions():
    print("To move left - press 'a'")
    print("To move right - press 'd'")
    print("To move down - press 's'")
    print("To move up - press 'w'")


def place_two_initial_elements_on_board(board):
    initial_element_value = 2
    get_fields_with_zero_value(board)

    first_initial_element = random.choice(get_fields_with_zero_value(board))
    first_initial_element.value = initial_element_value

    second_initial_element = random.choice(get_fields_with_zero_value(board))
    second_initial_element.value = initial_element_value


def get_random_number(max_range):
    return random.randint(0, max_range - 1)


def not_sorted_move_left_and_up(array):
    for index in range(0, len(array) - 1):
        while array[index].value == 0 and array[index + 1].value > 0:
            return True
    return False

def left_and_up_sort(array):
    for index in range(0, len(array) - 1):
        if array[index].value == 0 and array[index + 1].value > 0:
            temp_index = array[index].value
            temp_index_plus_one = array[index + 1].value
            array[index].value = temp_index_plus_one
            array[index + 1].value = temp_index


def move_left(board):
    for row in board:
        while not_sorted_move_left_and_up(row):
            left_and_up_sort(row)
    return board


def move_up(board):
    for column in get_columns(board) :
        while not_sorted_move_left_and_up(column):
            left_and_up_sort(column)
    return board


def not_sorted_move_right_and_down(row):
    for index in range(len(row) - 1, 0, -1):
        while row[index].value == 0 and row[index - 1].value > 0:
            return True
    return False


def right_and_down_sort(array):
    for index in range(len(array) - 1, 0, -1):
        if array[index].value == 0 and array[index - 1].value > 0:
            temp_index = array[index].value
            temp_index_minus_one = array[index - 1].value
            array[index - 1].value = temp_index
            array[index].value = temp_index_minus_one


def move_right(board):
    for row in board:
        while not_sorted_move_right_and_down(row):
            right_and_down_sort(row)
    return board


def move_down(board):
    for column in get_columns(board):
        while not_sorted_move_right_and_down(column):
            right_and_down_sort(column)
    return board


def right_or_down_sum(array):
    for index in range(len(array) - 1, 0, -1):
        if array[index].value == array[index - 1].value:
            array[index].value += array[index - 1].value
            array[index - 1].value = 0


def sum_right(board):
    for row in board:
        right_or_down_sum(row)
    return board


def sum_down(board):
    for column in get_columns(board):
        right_or_down_sum(column)
    return board


def left_or_up_sum(array):
    for index in range(0, len(array) - 1):
        if array[index].value == array[index + 1].value:
            array[index].value += array[index + 1].value
            array[index + 1].value = 0


def sum_left(board):
    for row in board:
        left_or_up_sum(row)
    return board


def sum_up(board):
    for column in get_columns(board):
        left_or_up_sum(column)
    return board


def get_fields_with_zero_value(board):
    fields_with_zero_value = []
    for row in board:
        for field in row:
            if field.value == 0:
                fields_with_zero_value.append(field)
    return fields_with_zero_value

def place_next_element_on_board(board):
    if len(get_fields_with_zero_value(board)) > 0:
        next_field = random.choice(get_fields_with_zero_value(board))
        next_field.value = 2


def check_if_similar_neighboring(board):
    for row in board:
        for index in range(0, len(row)-1):
            if row[index].value == row[index + 1].value:
                return True
    for column in get_columns(board):
        for index in range(0, len(column)-1):
            if column[index].value == column[index + 1].value:
                return True
    return False



def game_over(board):
    if len(get_fields_with_zero_value(board)) > 0:
        return False
    if check_if_similar_neighboring(board):
        return False
    print_board(board)
    print("You lost!")
    return True


def check_if_won(board):
    winning_number = 2048
    for row in board:
        for field in row:
            if field.value == winning_number:
                return True
    return False


def get_board_values(board):
    board_values = []
    for row in board:
        for field in row:
            board_values.append(field.value)
    return board_values

def validated_players_move(board):
    temporary_values_board = get_board_values(board)
    players_move = str(input("Next move: ").lower())
    if players_move == "a":
        move_left(board)
        sum_left(board)
        move_left(board)
        values_board = get_board_values(board)
        check_if_move_is_valid(board, temporary_values_board, values_board)
    elif players_move == "w":
        move_up(board)
        sum_up(board)
        move_up(board)
        values_board = get_board_values(board)
        check_if_move_is_valid(board, temporary_values_board, values_board)
    elif players_move == "d":
        move_right(board)
        sum_right(board)
        move_right(board)
        values_board = get_board_values(board)
        check_if_move_is_valid(board, temporary_values_board, values_board)
    elif players_move == "s":
        move_down(board)
        sum_down(board)
        move_down(board)
        values_board = get_board_values(board)
        check_if_move_is_valid(board, temporary_values_board, values_board)


def check_if_move_is_valid(board, temporary_values_board, values_board):
    if temporary_values_board == values_board:
        print("INVALID MOVE!")
    else:
        place_next_element_on_board(board)


def game(number_of_rows, number_of_columns):
    board = create_board(number_of_rows, number_of_columns)
    instructions()
    place_two_initial_elements_on_board(board)
    while not game_over(board):
        print_board(board)
        validated_players_move(board)
        if check_if_won(board) == True:
            print("You did it!")
            print_board(board)
            break

game(4, 4)