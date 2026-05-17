# Problem 13: Check if a number is a palindrome

n = int(input("Enter a number: "))
original = n
reversed_num = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if original == reversed_num:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is NOT a Palindrome")
