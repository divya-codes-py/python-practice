import random

secret = random.randint(1, 10)
count = 0

print("Welcome to the Guessing Game!")

while True:
    guess = int(input("Enter your guess (1-10): "))
    count = count + 1

    if guess == secret:
        print(f"🎉 Correct! You guessed it in {count} tries!")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
Step 5:
