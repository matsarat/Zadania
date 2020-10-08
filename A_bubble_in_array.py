from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

answer = []

for list in data:
    step_counts = 0
    for index in range(0, len(list)):
        if index + 1 < len(list):
            first = list[index]
            next = list[index + 1]
            if first > next:
                list[index] = next
                list[index + 1] = first
                step_counts += 1
    answer.append(step_counts)

seed = 113
limit = 10000007
result = 0
for number in list:
    result = (result + number) * seed
    if result > limit:
        result = result % limit
answer.append(result)

print(*list)
print(step_counts)
print(*answer)


