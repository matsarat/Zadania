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

    get_fields_with_zero_value(board)
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
    for index in range(0, len(array) - 1):
        if array[index].value == array[index + 1].value:
            array[index + 1].value += array[index].value
            array[index].value = 0


def sum_right(board):
    for row in board:
        right_or_down_sum(row)
    return board


def sum_down(board):
    for column in get_columns(board):
        right_or_down_sum(column)
    return board


def left_or_up_sum(array):
    for index in range (len(array) -1, 0, -1):
        if array[index].value == array[index - 1].value:
            array[index -1].value += array[index].value
            array[index].value = 0


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
    next_field = random.choice(get_fields_with_zero_value(board))
    next_field.value = 2


def game_over(board):
    winning_number = 2048
    for row in board:
        if winning_number in row:
            print("You did it!")
            return True
    if len(get_fields_with_zero_value(board)) > 0:
        return False
    if len(get_fields_with_zero_value(board)) == 0:
        print("YOU LOST!")
        return True


def valid_players_move(board):
    players_move = str(input("Next move: ").lower())
    if players_move == "a":
        move_left(board)
        sum_left(board)
        move_left(board)
    elif players_move == "w":
        move_up(board)
        sum_up(board)
        move_up(board)
    elif players_move == "d":
        move_right(board)
        sum_right(board)
        move_right(board)
    elif players_move == "s":
        move_down(board)
        sum_down(board)
        move_down(board)


def game(number_of_rows, number_of_columns):
    board = create_board(number_of_rows, number_of_columns)
    instructions()
    place_two_initial_elements_on_board(board)
    print_board(board)
    while game_over(board) == False:
        valid_players_move(board)
        get_fields_with_zero_value(board)
        game_over(board)
        place_next_element_on_board(board)
        print_board(board)

game(2, 2)