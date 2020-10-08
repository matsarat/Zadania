from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_float(" ")
print(data)

dice_rolling_results = []
for line in data:
    for number in line:
        dice_rolling_results.append((int(number * 6)+1))

print(*dice_rolling_results)