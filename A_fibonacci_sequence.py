from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_table_int(" ")
print(data)


number_indices_list = []

for line in data:
    number_index = 1
    fibonacci_sequence = []
    a = 0
    b = 1
    fibonacci_sequence.append(a)
    fibonacci_sequence.append(b)
    for number in line:
        if number == 0:
            number_index = 0
        else:
            while number not in fibonacci_sequence:
                c = a + b
                fibonacci_sequence.append(c)
                a = b
                b = c
                number_index += 1
        number_indices_list.append(number_index)

print(*number_indices_list)



