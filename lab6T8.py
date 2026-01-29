class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    pass

class Manager(Employee):
    def show_name(self):
        print(f"Manager Name: {self.name}")

mgr = Manager("Sarah")
mgr.show_name()