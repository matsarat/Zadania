from data_reader import DataReader
data_reader = DataReader("sums_in_loop.txt")
data = data_reader.get_lines()
print(data)

cleared_lines = []
for line in data:
    line = line.lower()
    alpha_line = ""
    for index in range(0, len(line)):
        if line[index].isalpha():
            alpha_line += line[index]
    cleared_lines.append(alpha_line)

print(cleared_lines)

palindromes_list = []
for cleared_line in cleared_lines:
    palindrome = ""
    index = len(cleared_line)-1
    while index > -1:
        palindrome += cleared_line[index]
        index -= 1
    palindromes_list.append(palindrome)

print(palindromes_list)

if_palindrome = []

for index in range(0, (len(palindromes_list))):
    if palindromes_list[index] == cleared_lines[index]:
        if_palindrome.append("Y")
    else:
        if_palindrome.append("N")

print(*if_palindrome)






