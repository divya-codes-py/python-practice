class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def display(self):
        print(f"\nBook: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {'Yes' if self.available else 'No'}")
    
    def issue(self, person):
        if self.available:
            self.available = False
            print(f"\n✅ Book issued to {person}!")
            print(f"Available: No")
        else:
            print("\n❌ Book not available!")
    
    def returnbook(self):
        self.available = True
        print("\n✅ Book returned!")
        print("Available: Yes")

b1 = Book("Python Basics", "Guido")
print("📚 Library System")
b1.display()
b1.issue("Divya")
b1.returnbook()
b1.issue("Ravi")
b1.issue("Ravi")
