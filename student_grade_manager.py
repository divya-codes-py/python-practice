class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
    
    def add_marks(self, mark):
        self.marks.append(mark)
    
    def display(self):
        average = sum(self.marks) / len(self.marks)
        highest = max(self.marks)
        lowest = min(self.marks)
        
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {round(average, 1)}")
        print(f"Highest: {highest}")
        print(f"Lowest: {lowest}")
        
        if average >= 80:
            print("Grade: A 🌟")
        elif average >= 60:
            print("Grade: B 👍")
        else:
            print("Grade: C 📚")

s1 = Student("Divya")
s1.add_marks(85)
s1.add_marks(90)
s1.add_marks(78)
s1.add_marks(92)
s1.add_marks(88)
s1.display()
Arthaaitaa? Try maadu! 😊💪
