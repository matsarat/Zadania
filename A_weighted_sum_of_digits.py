from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")

data = data_reader.get_table(" ")
print(data)

for list in data:
    results = []
    for number in list:
        wsd = 0
        iterations = len(number)
        for index in range(0, iterations):
            wsd += ((index+1) * int(number[index]))
        results.append(wsd)

print(*results)



