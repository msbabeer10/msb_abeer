def get_factorial(n):
    if n < 0: return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example use:
print("Factorial:", get_factorial(5))