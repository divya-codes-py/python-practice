sentence = "Python is awesome and Python is fun"

word_lengths = {word: len(word) for word in sentence.split()}
print("Word lengths:")
for word, length in word_lengths.items():
    print(f"  {word}: {length}")
