temp = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
wind = float(input("Enter wind speed (km/h): "))

if temp < 25 and humidity < 50 and wind < 15:
    print("Weather: Pleasant")
elif 25 <= temp <= 35 or 50 <= humidity <= 70:
    print("Weather: Normal")
else:
    print("Weather: Harsh")