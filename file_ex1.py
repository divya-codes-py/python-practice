# Write
with open("students.txt", "w") as f:
    f.write("Divya\n")
    f.write("Rahul\n")
    f.write("Priya\n")
    f.write("Kiran\n")
    f.write("Suma\n")

print("✅ File write aythu!")

# Read
with open("students.txt", "r") as f:
    content = f.read()
    print("\n📄 Students list:")
    print(content)
