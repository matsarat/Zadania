from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

results = []
for lisst in data:
    lisst.sort()
    counter = [x for x in range(1, 21)]
    index = len(counter)
    while index > 0:
        number_count = 0
        for element in lisst:
            if element == index:
                number_count += 1
        results.append(number_count)
        index -= 1

results.reverse()
print(*results)
