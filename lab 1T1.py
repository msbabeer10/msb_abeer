import math

# 1. Get the radius from the user
# We use float() to allow decimal numbers (e.g., 5.5)
radius = float(input("Enter the radius of the circle: "))

# 2. Calculate the area
# math.pi gives the value of Pi
# ** 2 creates the square of the radius
area = math.pi * (radius ** 2)

# 3. Display the result
# :.2f formats the number to 2 decimal places
print(f"The area of the circle is: {area:.2f}")
