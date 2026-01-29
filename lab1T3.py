# 1. Get the temperature in Celsius from the user
# We use float() because temperatures often have decimal points (e.g., 36.6)
celsius = float(input("Enter temperature in Celsius: "))

# 2. Convert to Fahrenheit
# Formula: (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# 3. Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
