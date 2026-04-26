def read_file_lines(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"❌ '{filename}' file sikkala!")

# Test file create maadi
with open("test.txt", "w") as f:
    f.write("Python is great\n")
    f.write("Generators are powerful\n")
    f.write("Memory efficient coding\n")
    f.write("yield keyword is amazing\n")

print("📄 File lines:")
for i, line in enumerate(read_file_lines("test.txt"), 1):
    print(f"  Line {i}: {line}")
