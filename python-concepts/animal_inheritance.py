class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(f"Animal: {self.name}")
        print(f"Sound: {self.sound}")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog", "Woof! 🐕")
        self.breed = breed
    
    def fetch(self):
        print(f"Breed: {self.breed}")
        print("Fetching the ball! 🎾")

class Cat(Animal):
    def __init__(self, breed):
        super().__init__("Cat", "Meow! 🐈")
        self.breed = breed
    
    def purr(self):
        print(f"Breed: {self.breed}")
        print("Purring... 😸")

d1 = Dog("Labrador")
d1.speak()
d1.fetch()

print()

c1 = Cat("Persian")
c1.speak()
c1.purr()
