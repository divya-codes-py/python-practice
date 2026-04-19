
# Write
with open("story.txt", "w") as f:
    f.write("Python is a great programming language\n")
    f.write("It is easy to learn and very powerful\n")
    f.write("Python is used in web development and data science\n")
    f.write("I love Python because it is simple and clean\n")

# Statistics
with open("story.txt", "r") as f:
    lines = f.readlines()

total_lines = len(lines)
total_words = sum(len(line.split()) for line in lines)
total_chars = sum(len(line) for line in lines)
longest_line = max(lines, key=len).strip()

# Most used word
all_words = " ".join(lines).split()
word_count = {}
for word in all_words:
    word_count[word] = word_count.get(word, 0) + 1
most_used = max(word_count, key=word_count.get)

print(f"📄 Total lines: {total_lines}")
print(f"📝 Total words: {total_words}")
print(f"🔤 Total characters: {total_chars}")
print(f"📏 Longest line: '{longest_line}'")
print(f"🔁 Most used word: '{most_used}' — {word_count[most_used]} times")
