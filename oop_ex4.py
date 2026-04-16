class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(f"✅ Marks set: {marks}")
        else:
            print("⚠️ Marks 0-100 naduva irali!")

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 70:
            return "C"
        else:
            return "D"

student = Student("Divya")
student.set_marks(92)
print(f"Marks: {student.get_marks()}")
print(f"Grade: {student.grade()}")
