password = input("Enter your password: ")
length = len(password)

if length < 6:
    print("Strength: Weak")
elif length < 10:
    print("Strength: Medium")
else:
    print("Strength: Strong")