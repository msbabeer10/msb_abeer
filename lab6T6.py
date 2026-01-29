class Grandparent:
    grandparent_name = "Robert"

class Parent(Grandparent):
    parent_name = "William"

class Child(Parent):
    def show_family(self):
        print(f"GP: {self.grandparent_name}, Parent: {self.parent_name}")

ch = Child()
ch.show_family()