
my_dict = {1: "barszcz", 2: "ogurkowa", 3: "rzurek"}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for key in my_dict:
    print(key, my_dict[key])

even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
print(even_squares)

cubes_by_four = [num ** 3 for num in range(1, 11) if (num ** 3) % 4 == 0]
print(cubes_by_four)

to_21 = [x for x in range(1, 22)]
print(to_21)

odds = to_21[::2]
print(odds)

middle_third = to_21[8:15:1]
print(middle_third)

squares = [x ** 2 for x in range(1, 11)]
print(squares)

filtered = (filter(lambda x: x in range(30, 71), squares))
print(filtered)