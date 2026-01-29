colors = {"Red", "Green", "Blue", "Yellow"}

# remove() raises an error if the item is missing
colors.remove("Red")

# discard() does NOT raise an error if the item is missing
colors.discard("Purple") 

print("Remaining colors:", colors)