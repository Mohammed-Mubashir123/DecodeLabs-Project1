# ==========================================
#      PASSWORD STRENGTH CHECKER
# ==========================================

import string

while True:

    print("\n" + "=" * 45)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    # Taking password input
    password = input("Enter your password: ")

    # Initial score
    score = 0

    print("\nSecurity Analysis:")
    print("-" * 45)

    # Password Length Check
    if len(password) >= 8:
        score += 1
        print("✔ Good password length")
    else:
        print("✖ Password should contain at least 8 characters")

    # Uppercase Check
    has_upper = any(char.isupper() for char in password)

    if has_upper:
        score += 1
        print("✔ Contains uppercase letter")
    else:
        print("✖ Missing uppercase letter")

    # Lowercase Check
    has_lower = any(char.islower() for char in password)

    if has_lower:
        score += 1
        print("✔ Contains lowercase letter")
    else:
        print("✖ Missing lowercase letter")

    # Digit Check
    has_digit = any(char.isdigit() for char in password)

    if has_digit:
        score += 1
        print("✔ Contains number")
    else:
        print("✖ Missing number")

    # Special Character Check
    has_symbol = any(char in string.punctuation for char in password)

    if has_symbol:
        score += 1
        print("✔ Contains special character")
    else:
        print("✖ Missing special character")

    # Final Result
    print("\n" + "=" * 45)
    print("FINAL RESULT")
    print("=" * 45)

    # Password Strength Classification
    if score <= 2:
        print("Password Strength: WEAK")
    elif score == 3 or score == 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: STRONG")

    # Security Score
    print(f"Security Score: {score}/5")

    # Suggestions
    print("\nSuggestions to Improve Security:")

    if len(password) < 8:
        print("- Increase password length")

    if not has_upper:
        print("- Add uppercase letters")

    if not has_lower:
        print("- Add lowercase letters")

    if not has_digit:
        print("- Add numbers")

    if not has_symbol:
        print("- Add special characters")

    # Perfect Password
    if score == 5:
        print("- Excellent password security!")

    print("=" * 45)

    # Retry System
    choice = input("\nDo you want to check another password? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using Password Strength Checker!")
        break