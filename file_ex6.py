# Source file create
with open("source.txt", "w") as f:
    f.write("Python is awesome!\n")
    f.write("I love coding!\n")
    f.write("Practice makes perfect!\n")

# Read source
with open("source.txt", "r") as f:
    content = f.read()

# Copy to destination
with open("destination.txt", "w") as f:
    f.write(content)

print("✅ File copy aythu!")

# Verify
with open("destination.txt", "r") as f:
    print("\n📄 Destination file:")
    print(f.read())
