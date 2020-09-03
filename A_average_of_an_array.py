from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")

data = data_reader.get_table_int(" ")
print(data)
results = []
for line in data:
    sum_of_array = 0
    average = 0
    for number in line:
        sum_of_array += number
        average = sum_of_array / (len(line) - 1)
    if average == int(average) + 0.5:
        results.append(int(average) + 1)
    else:
        results.append(round(average))

print(*results)



