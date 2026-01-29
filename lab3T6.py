price = float(input("Enter the total purchase price: "))

if price >= 1000:
    final_price = price * 0.80  # 20% off
elif price >= 500:
    final_price = price * 0.90  # 10% off
else:
    final_price = price

print(f"The final price after discount is: {final_price}")