# Write marks files
with open("math.txt", "w") as f:
    f.write("85\n90\n78\n")

with open("science.txt", "w") as f:
    f.write("92\n88\n95\n")

with open("english.txt", "w") as f:
    f.write("76\n82\n89\n")

print("✅ Ella files write aythu!\n")

# Read & calculate
subjects = ["math", "science", "english"]
all_marks = []

for subject in subjects:
    with open(f"{subject}.txt", "r") as f:
        marks = [int(line.strip()) for line in f.readlines()]
    average = sum(marks) / len(marks)
    all_marks.extend(marks)
    print(f"📚 {subject.title()} average: {round(average, 2)}")

overall = sum(all_marks) / len(all_marks)
print(f"\n🏆 Overall average: {round(overall, 2)}")
