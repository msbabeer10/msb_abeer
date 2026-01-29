class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def update_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary update.")

    def show_salary(self):
        print(f"Current Salary: {self.__salary}")

# Usage
emp = Employee(5000)
emp.update_salary(5500)
emp.show_salary()