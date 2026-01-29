# 1. Initialize an empty list
names = []

print("Please enter 5 names:")

# 2. Loop 5 times to get input
for i in range(5):
    # input() takes string input by default
    name = input(f"  Name {i+1}: ")
    
    # append() adds the new name to the end of the list
    # .strip() removes accidental spaces at the start or end
    names.append(name.strip())

# 3. Display the final list
print("\n--- Names Collected ---")
print(f"List: {names}")

# Optional: Loop through the list to print them cleanly
print("\nFormatted List:")
for name in names:
    print(f"- {name}")
