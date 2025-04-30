 # List of common weak password patterns
common_patterns = ['123', 'password', 'qwerty', 'abc', 'letmein']

def check_password_strength(password):
    strength = 0
    reasons = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        reasons.append("Too short")

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        strength += 1
    else:
        reasons.append("No uppercase letter")

    # Check for lowercase letters
    if any(c.islower() for c in password):
        strength += 1
    else:
        reasons.append("No lowercase letter")

    # Check for digits
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        reasons.append("No digit")

    # Check for special characters
    if any(not c.isalnum() for c in password):
        strength += 1
    else:
        reasons.append("No symbol")

    # Check for common patterns
    if any(pattern in password.lower() for pattern in common_patterns):
        reasons.append("Contains common pattern")

    # Give feedback
    print("\nPassword Analysis:")
    if strength >= 4 and 'Contains common pattern' not in reasons:
        print("Strength: Strong ")
    elif strength >= 3:
        print("Strength: Medium ")
    else:
        print("Strength: Weak ")

    # Show reasons
    if reasons:
        print("Issues:")
        for r in reasons:
            print(f"- {r}")

# Run the analyzer
user_input = input("Enter your password: ")
check_password_strength(user_input)
