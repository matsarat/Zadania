def remove_duplicates(elements):
    without_duplicates = []
    for element in elements:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

print(remove_duplicates([1, 1, 1, 2, 2, 3, 3, 4, 5]))