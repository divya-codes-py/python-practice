# Write
with open("paragraph.txt", "w") as f:
    f.write("python is great and python is easy\n")
    f.write("i love python because python is powerful\n")
    f.write("python helps me solve problems every day\n")

# Word count
with open("paragraph.txt", "r") as f:
    content = f.read()

words = content.split()
print(f"📄 Total words: {len(words)}")

# Most repeated word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_repeated = max(word_count, key=word_count.get)
print(f"🔁 Most repeated: '{most_repeated}' — {word_count[most_repeated]} times")
