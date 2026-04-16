class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says: {self.sound}")

class Dog(Animal):
    def fetch(self):
        print(f"{self.name} is fetching the ball! 🎾")

class Cat(Animal):
    def purr(self):
        print(f"{self.name} is purring... 😺")

dog = Dog("Tommy", "Woof!")
cat = Cat("Kitty", "Meow!")

dog.speak()
dog.fetch()
cat.speak()
cat.purr()
