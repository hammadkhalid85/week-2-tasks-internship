# Voting Eligibility
current_year = 2025
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

print(f"You are {age} years old.")
if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote yet.")
