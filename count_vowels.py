word = input("Enter a word: ")
vowels = 0
consonants = 0

for letter in word:
    if letter in "aeiou":
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
