# 1. Initialize a list with some existing data
fruits = ["Apple", "Banana", "Cherry"]
print(f"Original list: {fruits}")

# 2. Get a new item from the user
new_fruit = input("Enter a fruit to add to the end of the list: ")

# 3. Add the element to the end using append()
# This modifies the original list in place
fruits.append(new_fruit)

# 4. Display the updated list
print(f"Updated list:  {fruits}")
