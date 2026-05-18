# Count digits in a number

num = int(input("Enter a number: "))

count = 0

while True:
    num = num // 10
    count += 1

    if num == 0:
        break

print("Number of digits:", count)
