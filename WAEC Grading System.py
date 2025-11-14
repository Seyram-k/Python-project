print("=== WAEC Grading System ===")

score = float(input("Enter the student's score (0-100): ")) # Assume user enters a number

# Check for invalid scores first
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
else:
# Determine grade
    if 80 <= score <= 100:
        grade = 'A'
    elif 70 <= score <= 79:
        grade = 'B'
    elif 60 <= score <= 69:
        grade = 'C'
    elif 50 <= score <= 59:
        grade = 'D'
    elif 40 <= score <= 49:
        grade = 'E'
    else: # score < 40
        grade = 'F'

    print(f"The grade for a score of {score} is: {grade}")
