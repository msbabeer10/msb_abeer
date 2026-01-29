# Create a nested tuple
nested = ("Main", (100, 200, 300), "End")

# Access the second element (the inner tuple)
inner = nested[1]

# Access the second element inside that inner tuple (200)
value = nested[1][1]

print("Inner tuple:", inner)
print("Specific element from inner tuple:", value)