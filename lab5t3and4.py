class Student:
    def __init__(self, name, marks):
        # marks is expected to be a list or tuple of 3 numbers
        self.name = name
        self.marks = marks

    def get_average(self):
        avg = sum(self.marks) / len(self.marks)
        print(f"{self.name}'s Average Mark: {avg:.2f}")
        return avg

    def check_status(self, passing_mark=50):
        avg = sum(self.marks) / len(self.marks)
        if avg >= passing_mark:
            print(f"Status: PASSED")
        else:
            print(f"Status: FAILED")

# Example usage
s1 = Student("Alice", [85, 90, 78])
s1.get_average()
s1.check_status()