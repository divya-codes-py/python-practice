# Problem 10: Product of all digits of a number

n = int(input("Enter a number: "))
product = 1
temp = abs(n)
while temp > 0:
    digit = temp % 10
    product *= digit
    temp //= 10
print(f"Product of digits of {n} = {product}")
