class Account:
    def __init__(self, account_number, balance):
        self.account_no = account_number
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"Credited: ${amount}")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Debited: ${amount}")

    def print_balance(self):
        print(f"Account {self.account_no} Balance: ${self.balance}")

# Example usage
my_acc = Account("ACC12345", 1000)
my_acc.credit(500)
my_acc.debit(200)
my_acc.print_balance()