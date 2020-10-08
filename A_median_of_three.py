from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")

print(data)
median_list = []

for line in data:
    line = sorted(line)
    median_list.append(line[1])

print(*median_list)
