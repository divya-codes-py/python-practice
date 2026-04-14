sentence = "python is great python is easy python is fun"

# Count each word
word_count = {}

for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print results
print("Word Count:")
for word, count in word_count.items():
    print(f"  {word}: {count}")
