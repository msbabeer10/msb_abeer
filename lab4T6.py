while True:
    user_input = input("Enter something (type 'stop' to quit): ")
    if user_input.lower() == "stop":
        print("Loop terminated.")
        break
    print(f"You entered: {user_input}")