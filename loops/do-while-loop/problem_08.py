# Check Armstrong number

num = int(input("Enter a number: "))

original = num
sum = 0

while True:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

    if num == 0:
        break

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
