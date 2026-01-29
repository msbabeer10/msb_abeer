# 1. Initialize a list
# We use a mixed list (strings and numbers) to show flexibility
items = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

print(f"Original list: {items}")

# --- METHOD 1: remove() ---
# remove(x) searches for the first occurrence of x and deletes it.
# It does NOT return the value. It raises an error if the value isn't found.
print("\n--- Using remove() ---")
item_to_remove = input("Enter the EXACT name of the item to remove (e.g., Mouse): ")

try:
    items.remove(item_to_remove)
    print(f"Successfully removed '{item_to_remove}'.")
except ValueError:
    print(f"Error: '{item_to_remove}' was not found in the list.")

print(f"List after remove: {items}")

# --- METHOD 2: pop() ---
# pop(i) removes the item at index i and RETURNS it.
# If no index is specified, it removes the last item.
print("\n--- Using pop() ---")
print("Current indices:")
for i, item in enumerate(items):
    print(f"  {i}: {item}")

try:
    index_input = input("Enter the index number to pop (leave empty to pop the last item): ")
    
    if index_input.strip() == "":
        # Pop the last item if input is empty
        popped_item = items.pop()
        print(f"Popped the last item: '{popped_item}'")
    else:
        # Pop the specific index
        index = int(index_input)
        popped_item = items.pop(index)
        print(f"Popped item at index {index}: '{popped_item}'")
        
except IndexError:
    print("Error: That index is out of range.")
except ValueError:
    print("Error: Please enter a valid number.")

# 3. Final Result
print(f"\nFinal list: {items}")
