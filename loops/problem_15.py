# Problem 15: Check if a number is an Armstrong number

n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is NOT an Armstrong number")
