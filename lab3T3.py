stored_user = "admin"
stored_pass = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_user and password == stored_pass:
    print("Login successful!")
else:
    print("Invalid credentials.")