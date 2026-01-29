# 1. Initialize variables
# We can store subject names in a list to make the input process cleaner
subjects = ["English", "Math", "Science", "History", "Computer"]
marks = []
max_marks_per_subject = 100

print("Enter marks obtained in 5 subjects (out of 100):")

# 2. Get input for each subject
for subject in subjects:
    # Input validation loop (optional but good practice)
    while True:
        try:
            score = float(input(f"  {subject}: "))
            if 0 <= score <= max_marks_per_subject:
                marks.append(score)
                break
            else:
                print("    Please enter a valid score between 0 and 100.")
        except ValueError:
            print("    Invalid input. Please enter a number.")

# 3. Calculate Total and Percentage
total_marks = sum(marks)
max_total_marks = max_marks_per_subject * len(subjects)
percentage = (total_marks / max_total_marks) * 100

# 4. Display Results
print("\n--- Results ---")
print(f"Total Marks Obtained: {total_marks} / {max_total_marks}")
print(f"Percentage: {percentage:.2f}%")

# Optional: Add a grade based on percentage
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
else:
    grade = 'D'

print(f"Grade: {grade}")
