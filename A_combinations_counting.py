from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

def factorial(num):
    factorial_res = 1
    while num > 0:
        factorial_res *= num
        num -= 1
    return factorial_res

combinations_list = []

for line in data:
    n = int(line[0])
    k = int(line[1])
    combinations = factorial(n) / (factorial(k) * factorial((n-k)))
    combinations_list.append(int(combinations))

print(*combinations_list)


