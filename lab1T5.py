# 1. Create a list of 5 numbers
# We'll ask the user to input them to make the program dynamic
numbers = []
print("Please enter 5 numbers:")

for i in range(5):
    while True:
        try:
            num = float(input(f"  Number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("  Invalid input. Please enter a number.")

# 2. Calculate Sum, Max, and Min
# Python provides built-in functions for these common operations
total_sum = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

# 3. Display the results
print("\n--- Statistics ---")
print(f"List:    {numbers}")
print(f"Sum:     {total_sum}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")