total = float(input("Enter total amount: "))

if total >= 500:
    discount = 0.20
elif total >= 200:
    discount = 0.10
else:
    discount = 0

amount_saved = total * discount
print(f"Discount: {discount*100}%. You saved: {amount_saved}")