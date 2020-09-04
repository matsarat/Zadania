from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)
seed = 113
limit = 10000007

for array in data:
    result = 0
    for number in array:
        result = (result + number) * seed
        if result > limit:
            result = result % limit

print(result)

