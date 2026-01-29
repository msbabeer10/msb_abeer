class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display_details(self):
        print(f"Student: {self.__name}, Marks: {self.__marks}")

# Usage
s1 = Student("Alice", 95)
s1.display_details()