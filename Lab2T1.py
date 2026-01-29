# 1. Create a tuple with 10 elements (Int, Float, String)
my_tuple = (10, "Python", 3.14, 10, "AI", 7, 10, "Data", 2.5, "Code")

# 2. Count a specific element using count()
count_10 = my_tuple.count(10)
print(f"The number 10 appears {count_10} times.")

# 3. Convert tuple to list, modify it, and convert it back
temp_list = list(my_tuple)
temp_list[1] = "Java"  # Modifying index 1
my_tuple = tuple(temp_list)
print("Modified Tuple:", my_tuple)

# 4. Create a nested tuple and access elements
nested_tuple = ("Fruit", ("Apple", "Banana", "Cherry"), 50)
inner_element = nested_tuple[1][1]  # Accessing 'Banana'
print("Accessed from inner tuple:", inner_element)