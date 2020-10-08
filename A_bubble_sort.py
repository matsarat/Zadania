from data_reader import DataReader

data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

answer = []


def not_sorted(lista):
    for index in range(0, len(lista) - 1):
        if (index + 1) < len(lista):
            if lista[index] > lista[index + 1]:
                return True
    return False


for list in data:
    step_counts = 1
    swap_counts = 0
    while not_sorted(list):
        step_counts += 1
        for index in range(0, len(list)):
            if index + 1 < len(list):
                first = list[index]
                next = list[index + 1]
                if first > next:
                    list[index] = next
                    list[index + 1] = first
                    swap_counts += 1
    answer.append(step_counts)
    answer.append(swap_counts)

print(*list)
print(swap_counts)
print(*answer)
