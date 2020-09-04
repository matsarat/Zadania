from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.lines
print(data)
reversed_string = ""
for string in data:
    index = (len(string) - 1)
    while index >= 0:
        reversed_string += string[index]
        index -= 1

print(reversed_string)