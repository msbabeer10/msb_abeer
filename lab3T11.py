def categorize_temp(temp):
    if temp < 10:
        return "Cold"
    elif 10 <= temp <= 25:
        return "Warm"
    else:
        return "Hot"

# Example use:
print("The weather is:", categorize_temp(18))