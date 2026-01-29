class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

# Creating an object
my_car = Car("Tesla Model 3", "Midnight Silver")
print(f"Car Model: {my_car.model}")
print(f"Car Color: {my_car.color}")