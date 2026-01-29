class Device:
    type = "Electronic"

class Computer(Device):
    os = "Windows"

class Laptop(Computer):
    def display_brand(self, brand):
        print(f"Brand: {brand}, OS: {self.os}, Type: {self.type}")

lp = Laptop()
lp.display_brand("Dell")