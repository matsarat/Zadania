from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)


def swap(first, next):
    list[index + 1] = first
    list[index] = next

def not_sorted():
    for index in range(0, len(list)):
        if index + 1 < len(list):
            if list[index] > list[index + 1]:
                return True
        else:
            return False

unsorted = []
for list in data:
    while not_sorted():
        for index in range(0, len(list)):
            if index + 1 < len(list):
                first = list[index]
                next = list[index + 1]
                if first > next:
                    swap(first, next)

print(*unsorted)
print(list)


