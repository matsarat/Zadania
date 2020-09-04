from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")

print(data)

#a, b and c are lenghts of sides
results = []
for line in data:
    a = line[0]
    b = line[1]
    c = line[2]
    if (a < b + c) and (b < a + c) and (c < a + b):
        results.append("1")
    else:
        results.append("0")

print (*results)