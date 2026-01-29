# 1. Initialize a list
colors = ["Red", "Green", "Blue", "Yellow"]

print("Current list of colors:")
# Display list with indices so the user knows where to insert
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# 2. Get inputs from the user
new_color = input("\nEnter a color to insert: ")

# Input validation for the index is good practice
while True:
    try:
        position = int(input(f"Enter the index position (0 to {len(colors)}): "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# 3. Insert the element
# list.insert(index, element) adds the element BEFORE the given index.
colors.insert(position, new_color)

# 4. Display the updated list
print(f"\nUpdated list: {colors}")
