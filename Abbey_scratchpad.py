from data_reader import DataReader

data_reader = DataReader("sums_in_loop.txt")
print(data_reader.get_table_int(" "))

table = data_reader.get_table_int(" ")
result_table = []
for row in table:
    first_row = row[0]
    second_row = row[1]
    remainder = first_row % second_row
    division_result = first_row / second_row
    if division_result > 0:
        if division_result == (int(division_result) + 0.5):
            division_result = int(division_result) + 1
        else:
            division_result = round(division_result)
    elif division_result < 0:
        if division_result == (int(division_result) - 0.5):
            division_result = int(division_result)
        else:
            division_result = round(division_result)

    result_table.append(int(division_result))

print(*result_table)







