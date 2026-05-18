# Find largest number until 0 is entered

largest = 0

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    if num > largest:
        largest = num

print("Largest number is:", largest)
