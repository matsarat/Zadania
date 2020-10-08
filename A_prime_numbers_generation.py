
def is_prime(num):
    for x in range(2, int((num/2)+1)):
        if num % x == 0:
            return False
    else:
        prime_numbers.append(num)

num = 2
while len(prime_numbers) < 2000:
    is_prime(num)
    num += 1

print(prime_numbers)






