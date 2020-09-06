from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.lines
print(data)

starter = int(data[0])
operations = data[1::]
operations_splitted = []
result = 0
result += starter
for operation in operations:
    operations_splitted.append(operation.split(" "))


for list in operations_splitted:
    if list[0] == "*":
        result *= int(list[1])
    elif list[0] == "+":
        result += int(list[1])
    else:
        result = result % int(list[1])


print(result)
