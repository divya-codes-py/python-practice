class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: ₹{self.price}")
        print("-" * 25)

car1 = Car("Toyota", "Innova", 2022, 1500000)
car2 = Car("Hyundai", "i20", 2023, 800000)

car1.display_info()
car2.display_info()
