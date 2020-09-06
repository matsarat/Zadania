from data_reader import DataReader

data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

"""
v - rooted value
d - some crazy variable
r - root
"""


def get_d(value, r):
    return value / r


def get_r(r, d):
    return (r + d) / 2


def square(value, iterations, r=1):
    while iterations > 0:
        d = get_d(value, r)
        r = get_r(r, d)
        iterations -= 1
    return r


def break_number_to(number):
    return str(rounded).split('.')


def is_integer(list_with_broken_number_to_string_list):
    return len(list_with_broken_number_to_string_list) == 1 or \
           int(list_with_broken_number_to_string_list[1]) == 0


def get_integer_if_number_is_integer(number):
    list_with_broken_number_to_string_list = break_number_to(number)
    if is_integer(list_with_broken_number_to_string_list):
        return int(number)
    else:
        return number


results = []

for line in data:
    value = line[0]
    iterations = line[1]
    r = square(value, iterations)
    if r != int:
        rounded = round(r, 10)
        results.append(get_integer_if_number_is_integer(rounded))
    else:
        results.append(int(r))

print(*results)
