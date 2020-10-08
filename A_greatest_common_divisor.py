from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)

gcd_list = []
lcm_list = []

result_list = []

for line in data:
    a = line[0]
    b = line[1]
    gcd = 0
    lcm = 0
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    gcd_list.append(a)
    lcm = int((line[0] * line[1]) / a)
    gcd = a
    lcm_list.append(lcm)
    result_list.append("(" + str(gcd) + " " + str(lcm) + ")")

print(*result_list)
