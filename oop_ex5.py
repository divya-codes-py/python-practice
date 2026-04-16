class Car:
    def drive(self):
        print("🚗 Car is driving!")

class Airplane:
    def fly(self):
        print("✈️ Airplane is flying!")

class FlyingCar(Car, Airplane):
    def display(self):
        print("🚗✈️ Flying Car ready!")

flying_car = FlyingCar()
flying_car.display()
flying_car.drive()
flying_car.fly()
