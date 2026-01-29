class Employee:
    def __init__(self, emp_id, name, salary):
        self.id = emp_id
        self.name = name
        self.salary = salary # Monthly salary

    def display_annual_salary(self):
        annual = self.salary * 12
        print(f"Employee: {self.name} (ID: {self.id})")
        print(f"Annual Salary: ${annual}")

# Example usage
emp1 = Employee(101, "John Doe", 5000)
emp1.display_annual_salary()