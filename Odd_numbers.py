def purify(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            odd_numbers.append(number)
    return odd_numbers