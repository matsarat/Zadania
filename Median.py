def median(numbers):
    numlist = sorted(numbers)
    if len(numlist) % 2 != 0:
        return numlist[len(numlist) // 2]

    elif len(numlist) % 2 == 0:
        ind1 = int(len(numlist) / 2)
        ind2 = int(len(numlist) / 2 - 1)

        return (numlist[ind1] + numlist[ind2]) / 2.0

print(median([1]))
print(median([1, 2, 3, 4, 5]))
print(median([1, 2, 3, 4, 5, 6, 7, 8]))