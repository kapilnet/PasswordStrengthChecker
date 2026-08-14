import re

def check_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []

    # 1. Check Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Must be at least 8 characters long.")

    # 2. Check Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing an uppercase letter (A-Z).")

    # 3. Check Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing a lowercase letter (a-z).")

    # 4. Check Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Missing a number (0-9).")

    # 5. Check Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Missing a special character (e.g., !, @, #, $).")

    # Determine final rating based on score
    if score <= 2:
        rating = "WEAK"
    elif score <= 4:
        rating = "MEDIUM"
    else:
        rating = "STRONG"

    return rating, feedback

# Main program loop
print("--- Cybersecurity Password Strength Auditor ---")
user_password = input("Enter a password to test: ")
rating, improvements = check_password_strength(user_password)

print(f"\nPassword Rating: {rating}")
if improvements:
    print("Suggestions to improve security:")
    for suggestion in improvements:
        print(suggestion)
