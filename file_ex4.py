# Write
with open("fruits.txt", "w") as f:
    f.write("apple\nbanana\nmango\ngrape\norange\n")

# Search
fruit = input("Yaavudu fruit search maadali? ").lower()

with open("fruits.txt", "r") as f:
    fruits = [line.strip() for line in f.readlines()]

if fruit in fruits:
    print(f"✅ '{fruit}' file alli iddhe!")
else:
    print(f"❌ '{fruit}' file alli illa!")
