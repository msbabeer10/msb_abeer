dict_one = {"id": 1, "name": "Admin"}
dict_two = {"role": "Superuser", "access": "Full"}

# Merge dict_two into dict_one
dict_one.update(dict_two)
print("Merged Dictionary:", dict_one)