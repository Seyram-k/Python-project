print("--- EC Voting Eligibility System ---")

name = input("Enter your full name: ").strip()
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").strip().lower()

# Check eligibility conditions
if age >= 18 and (nationality == "ghanaian"):
    print(f"\nCongratulations, {name}! You are eligible to vote in Ghana.")
else:
    print(f"\nSorry, {name}. You are not eligible to vote.")
    if age < 18:
        print("This is because you are under 18 years old.")
    if nationality != "ghanaian":
        print("This is because you are not a Ghanaian citizen.")
