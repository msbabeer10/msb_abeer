# 10. Create dictionary of 3 students and print pairs
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
for key, value in students.items():
    print(f"Student: {key}, Mark: {value}")

# 11 & 13. Add new key-value pair using assignment
students["Diana"] = 88 

# 12. Access a value using its key
print("Bob's Mark:", students["Bob"])

# 14. Update an existing value
students["Alice"] = 90
print("Updated Alice's Mark:", students["Alice"])

# 15. Remove key-value pair using pop() and del
students.pop("Charlie")
del students["Alice"]

# 16. Use .items() to print in a loop
print("Current Dictionary items:")
for k, v in students.items():
    print(f"{k} -> {v}")

# 17. Find the number of items using len()
print("Total students remaining:", len(students))

# 18. Merge two dictionaries using update()
extra_data = {"Eve": 95, "Frank": 70}
students.update(extra_data)
print("Merged Dictionary:", students)