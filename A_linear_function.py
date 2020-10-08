from data_reader import DataReader


def get_A(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def get_B(x1, y1, x2, y2):
    return ((y1 * x2) - (y2 * x1)) / (x2 - x1)


data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)
results = []
for line in data:
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]

    a = get_A(x1, y1, x2, y2)
    b = get_B(x1, y1, x2, y2)
    results.append('('+ str(int(a)) + ' ' +str(int(b)) +')')
print(*results)
