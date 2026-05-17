# Problem 14: Sum of digits of a number

n = int(input("Enter a number: "))
total = 0
temp = abs(n)
while temp > 0:
    total += temp % 10
    temp //= 10
print(f"Sum of digits of {n} = {total}")
