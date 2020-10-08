from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_float(" ")
print(data)


result_list = []
for line in data:
    result_list.append(line[0])
    for index in range(0, len(line)-1):
        if index > 0:
            result_list.append(float(round(((line[index-1] + line[index] + line[index + 1]) / 3), 10)))
    result_list.append(line[len(line)-1])

print(*result_list)