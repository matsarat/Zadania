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
    number_of_rows = get_number_of_rows(board)
    number_of_columns = get_number_of_columns(board)

    first_row_number = get_random_number(number_of_rows)
    first_column_number = get_random_number(number_of_columns)
    board[first_row_number][first_column_number].value = initial_element_value

    second_row_number = get_random_number(number_of_rows)
    second_column_number = get_random_number(number_of_columns)
    while second_row_number == first_row_number and second_column_number == first_column_number:
        second_row_number = get_random_number(number_of_rows)
        second_column_number = get_random_number(number_of_columns)
    board[second_row_number][second_column_number].value = initial_element_value


def get_random_number(max_range):
    return random.randint(0, max_range - 1)


board = create_board(4, 4)
place_two_initial_elements_on_board(board)
print_board(board)


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
    print_board(board)
    return board

def move_up(board):
    for column in get_columns(board) :
        while not_sorted_move_left_and_up(column):
            left_and_up_sort(column)
    print_board(board)
    return board

move_left(board)

def not_sorted_move_right(row):
    for index in range(len(row) - 1, 0, -1):
        while row[index].value == 0 and row[index - 1].value > 0:
            return True
    return False

def move_right(board):
    for row in board:
        while not_sorted_move_right(row):
            right_and_down_sort(row)
    print_board(board)
    return board


def right_and_down_sort(array):
    for index in range(len(array) - 1, 0, -1):
        if array[index].value == 0 and array[index - 1].value > 0:
            temp_index = array[index].value
            temp_index_minus_one = array[index - 1].value
            array[index - 1].value = temp_index
            array[index].value = temp_index_minus_one


move_right(board)


