# Problem 25: Sum of all factors of a number

n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    if n % i == 0:
        total += i
    i += 1
print(f"Sum of factors of {n} = {total}")
