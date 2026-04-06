class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"{self.name} is a good student! 🌟")

# Object create maadu
s1 = Student("Divya", 17, "A")
s1.display()
