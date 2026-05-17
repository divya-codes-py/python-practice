# Problem 12: Reverse a number

n = int(input("Enter a number: "))
reversed_num = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
print(f"Reversed value of {n} = {reversed_num}")
