dic = {
    "id": 1,
    "NAme": "ahmad",
    "department": {1, 5, 6}
}
print(dic)
print(dic.keys())
print(dic.values())
print(dic["department"])
dic["Section"] = "C"
print(dic)
dic.pop("NAme")
print(dic.items())

dic.clear()
print(dic)
# del dic  # Commented out: can't print dic after deleting it