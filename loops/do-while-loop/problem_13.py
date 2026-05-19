# Count positive numbers until negative number is entered

count = 0

while True:
    num = int(input("Enter a number: "))

    if num < 0:
        break

    if num > 0:
        count += 1

print("Positive numbers count:", count)
