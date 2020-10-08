from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")

data = data_reader.lines
print(data)

vowels = "aeiouy"
vowel_count_list = []
for line in data:
    vowel_count = 0
    for letter in line:
        if letter in vowels:
            vowel_count += 1
    vowel_count_list.append(vowel_count)

print(*vowel_count_list)
