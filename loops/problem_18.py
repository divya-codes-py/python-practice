# Problem 18: Check if a given number is prime

n = int(input("Enter a number: "))
is_prime = True
if n < 2:
    is_prime = False
i = 2
while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print(f"{n} is a Prime number")
else:
    print(f"{n} is NOT a Prime number")
