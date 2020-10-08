from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

steps_list = []

for line in data:
    for number in line:
        opener = number
        sequence = []
        steps = 0
        sequence.append(number)
        while 1 not in sequence:
            if sequence[len(sequence) - 1] % 2 == 0:
                sequence.append((sequence[len(sequence) - 1]) / 2)
                steps += 1
            else:
                sequence.append((sequence[len(sequence) - 1]) * 3 + 1)
                steps += 1
        steps_list.append(steps)

print(*steps_list)





