set1 = {1, 0, True, "ahamd", 0, False, "ahamd"}
set2 = {4,6,2,1}
print(set1)

print(set2)
print(set1)
set1.add("HAmza")
print(set1)
set1.remove(0)
print(set1)
set1.update(set2)
print(set1)
print("union:", set1.union(set2))
print("intersection:", set1.intersection(set2))