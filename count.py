def count(sequence, item):
    total = 0
    for element in sequence:
        if element == item:
            total += 1
    return total


print(count([3, 1, 1, 2, 3, 1, 1, 3, 1], 2))
