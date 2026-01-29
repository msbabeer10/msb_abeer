def calculate_average(numbers):
    if not numbers: return 0
    return sum(numbers) / len(numbers)

# Example use:
nums = [10, 20, 30, 40]
print("Average:", calculate_average(nums))