# Problem 11: Total number of digits in a number

n = int(input("Enter a number: "))
count = 0
temp = abs(n)
if temp == 0:
    count = 1
while temp > 0:
    count += 1
    temp //= 10
print(f"Number of digits in {n} = {count}")
