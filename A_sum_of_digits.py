from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")

print(data)
results = []

for row in data:
    results.append(str((row[0] * row[1]) + row[2]))
    list_of_sums = []
    for result in results:
        sum_of_digits = 0
        for digit in result:
            sum_of_digits += int(digit)
        list_of_sums.append(sum_of_digits)





print(results)
print(*list_of_sums)
