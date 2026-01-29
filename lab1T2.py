# 1. Get the values from the user
# We use input() to get the values. They will be treated as strings, 
# which is fine for swapping.
x = input("Enter the first number (x): ")
y = input("Enter the second number (y): ")

print(f"\nOriginal values: x = {x}, y = {y}")

# 2. Swap the numbers
# Python allows this elegant syntax: "Tuple Unpacking"
# It evaluates the right side (y, x) first, creates a tuple, 
# and then assigns it to the left side (x, y).
x, y = y, x

# Alternative "Traditional" way (common in other languages):
# temp = x
# x = y
# y = temp

# 3. Display the result
print(f"Swapped values:  x = {x}, y = {y}")
