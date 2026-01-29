data = {"a": 1, "b": 2, "c": 3, "d": 4}

# Remove using pop (returns the value)
val = data.pop("a")

# Remove using del
del data["b"]

print("Dictionary after removals:", data)