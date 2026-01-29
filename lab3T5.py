speed = float(input("Enter speed (km/h): "))

if speed <= 60:
    print("No fine")
elif 60 < speed <= 80:
    print("Small fine")
else:
    print("Heavy fine")