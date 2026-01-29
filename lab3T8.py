def calculate_tax(price, tax_percentage):
    final_price = price + (price * (tax_percentage / 100))
    return final_price

# Example use:
print("Final Price:", calculate_tax(100, 15))