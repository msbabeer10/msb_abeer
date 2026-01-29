class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def show_student(self):
        print(f"Name: {self.name}, Age: {self.age}")

s = Student("John", 20)
s.show_student()