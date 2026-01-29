class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def display(self):
        print(f"Car: {self.brand} {self.model}")

c = Car("Toyota", "Corolla")
c.display()