# 5. Define a set of 7 elements
my_set = {1, 2.5, "Apple", 42, "Cloud", 9.9, "Tech"}

# 6. Add one element using add() and multiple using update()
my_set.add("NewItem")
my_set.update([100, "UpdateItem"])

# 7. Remove an element using remove() and discard()
my_set.remove("Apple")    # Raises error if element doesn't exist
my_set.discard("Cloud")   # Does NOT raise error if element is missing
print("Set after removals:", my_set)

# 8. Set Union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a.union(set_b))

# 9. Set Intersection
print("Intersection:", set_a.intersection(set_b))