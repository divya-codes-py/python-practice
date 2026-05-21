sentence = input("Enter a sentence: ")

# Words count
words = len(sentence.split())
print(f"Total words: {words}")

# Characters count
characters = len(sentence.replace(" ", ""))
print(f"Total characters: {characters}")

# Most repeated letter
sentence_lower = sentence.lower()
most_repeated = ""
max_count = 0

for letter in sentence_lower:
    if letter != " ":
        count = sentence_lower.count(letter)
        if count > max_count:
            max_count = count
            most_repeated = letter

print(f"Most repeated letter: {most_repeated}")
