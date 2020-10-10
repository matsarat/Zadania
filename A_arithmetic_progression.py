from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")

data = data_reader.get_table_int(" ")
print(data)

results = []
for line in data:
    sequence = []
    iterations = line[2]
    step = line[1]
    opener = line[0]
    factor = 0
    while iterations > 0:
        sequence.append(opener + step * factor)
        factor += 1
        iterations -= 1
    print(sequence)
    results.append(sum(sequence))

print(*results)