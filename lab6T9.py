class Academics:
    subject = "Mathematics"

class Sports:
    sport_name = "Basketball"

class Student(Academics, Sports):
    def display_all(self):
        print(f"Subject: {self.subject}, Sport: {self.sport_name}")

stu = Student()
stu.display_all()