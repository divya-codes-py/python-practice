with open("notes.txt", "w") as f:
    f.write("Python bahala channagide\n")
    f.write("Functions reusable code maaduttave\n")
    f.write("OOP real world problems solve maaduttade\n")
    f.write("File handling data store maaduttade\n")
    f.write("Practice maadidre improve aaguttire\n")

# Count & print lines
with open("notes.txt", "r") as f:
    lines = f.readlines()
    print(f"📄 Total lines: {len(lines)}\n")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")
