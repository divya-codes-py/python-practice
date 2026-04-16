# Write
with open("diary.txt", "w") as f:
    f.write("Ivattu channagittu!\n")

# Append
with open("diary.txt", "a") as f:
    f.write("Python kalidhe!\n")

# Read
with open("diary.txt", "r") as f:
    print("📔 Diary:")
    print(f.read())
