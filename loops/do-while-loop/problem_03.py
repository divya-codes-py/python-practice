# Sum of entered numbers until 0 is entered

total = 0

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    total += num

print("Sum is:", total)
