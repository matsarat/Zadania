from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)
for line in data:
    print(line.index(max(line)))

for line in data:
    biggest_indexes = []
    list_border = (len(line) - 1)
    while list_border > 0:
        biggest = max(line[:list_border+1])
        biggest_index = line.index(max(line[:list_border+1]))
        biggest_indexes.append(biggest_index)
        last = line[list_border]
        line[list_border] = biggest
        line[biggest_index] = last
        list_border -= 1
    print(line)
    print(*biggest_indexes)
