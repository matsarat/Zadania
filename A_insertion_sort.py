from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

swapped_elements_count_list = []

for line in data:
    for index in range(1, len(line)):
        temp_unsorted = line[index]
        swapped_elements = 0
        while line[index-1] > temp_unsorted and index > 0:
            line[index], line[index-1] = line[index-1], line[index]
            index -= 1
            swapped_elements += 1
        swapped_elements_count_list.append(swapped_elements)
print(*line)


print(*swapped_elements_count_list)