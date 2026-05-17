# Problem 17: Print all prime numbers between 1 and 100

i = 2
while i <= 100:
    is_prime = True
    j = 2
    while j * j <= i:
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        print(i, end=" ")
    i += 1
print()
