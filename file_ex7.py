import csv

# Write CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Divya", 20, "A"])
    writer.writerow(["Rahul", 21, "B"])
    writer.writerow(["Priya", 19, "A"])
    writer.writerow(["Kiran", 22, "C"])

print("✅ CSV file write aythu!\n")

# Read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    print(f"{'Name':<10} {'Age':<5} {'Grade':<5}")
    print("-" * 25)
    next(reader)  # Header skip
    for row in reader:
        print(f"{row[0]:<10} {row[1]:<5} {row[2]:<5}")
