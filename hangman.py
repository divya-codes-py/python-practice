import random

words = [
    "python", "computer", "keyboard", "program",
    "function", "variable", "loop", "string",
    "integer", "boolean"
]

def display(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("🎯 Hangman Game!")
    print("=" * 30)

    while attempts > 0:
        print(f"\nWord: {display(word, guessed)}")
        print(f"Guessed letters: {', '.join(guessed) if guessed else 'None'}")
        print(f"Attempts remaining: {attempts}")

        guess = input("Oru letter type maadi: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Ondu letter maatra type maadi!")
            continue

        if guess in guessed:
            print("⚠️ Ee letter already try maadiddiri!")
            continue

        guessed.append(guess)

        if guess in word:
            print("✅ Correct!")
            if all(letter in guessed for letter in word):
                print(f"\n🎉 Gెలిచಿರಿ! Word: {word}")
                break
        else:
            attempts -= 1
            print(f"❌ Tappu! {attempts} attempts ulididhe")

    else:
        print(f"\n💀 Game over! Word: '{word}' aagittu")

hangman()
