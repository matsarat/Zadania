from data_reader import DataReader

data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)


class Number(object):
    def __init__(self, value, initial_index):
        self.value = value
        self.initial_position = initial_index + 1

    def __str__(self):
        return str(self.initial_position)

    def __repr__(self):
        return str(self.initial_position)


def not_sorted(numbers):
    for index in range(0, len(numbers)):
        if index + 1 < len(numbers):
            if numbers[index].value > numbers[index + 1].value:
                return True
        else:
            return False


def swap(numbers, first, next, index):
    numbers[index + 1] = first
    numbers[index] = next


for lista in data:
    numbers = []
    for index in range(0, len(lista)):
        numbers.append(Number(lista[index], index))

    while not_sorted(numbers):
        for index in range(0, len(numbers)):
            if index + 1 < len(numbers):
                first = numbers[index]
                next = numbers[index + 1]
                if first.value > next.value:
                    swap(numbers, first, next, index)
    print(numbers)
