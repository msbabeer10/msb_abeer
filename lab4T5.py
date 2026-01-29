correct_password = "python123"

while True:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access Granted!")
        break
    else:
        print("Incorrect, try again.")