# Problem 16: Check if a number is a Perfect number

n = int(input("Enter a number: "))
total = 0
i = 1
while i < n:
    if n % i == 0:
        total += i
    i += 1
if total == n:
    print(f"{n} is a Perfect number")
else:
    print(f"{n} is NOT a Perfect number")
