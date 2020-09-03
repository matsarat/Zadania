from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_float(" ")

print(data)
bmi_results = []

for line in data:
    bmi_results.append(round(line[0] / line[1] ** 2, 3))
grades = []
for result in bmi_results:
    if result < 18.5:
        grades.append("under")
    elif result < 25:
        grades.append("normal")
    elif result < 30:
        grades.append("over")
    else:
        grades.append("obese")

print(bmi_results)
print(*grades)
