import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    else:
        return "Strong"


def main():
    print("🔐 Advanced Password Generator 🔐")

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid length!")
        return

    use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    num = int(input("How many passwords to generate? "))

    print("\nGenerated Passwords:\n")

    for i in range(num):
        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        strength = check_strength(pwd)
        print(f"{i+1}. {pwd}  --> Strength: {strength}")


if __name__ == "__main__":
    main()