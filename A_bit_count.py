from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

for line in data:
    binary_values = []
    for number in line:
        binary_values.append(bin(number))

print(binary_values)
bits_count_list = []

for binary_value in binary_values:
    bits_count = 0
    for index in range(len(binary_value)):
        if binary_value[index] == "1":
            bits_count += 1
    bits_count_list.append(bits_count)

print(*bits_count_list)




