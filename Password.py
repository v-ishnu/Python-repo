"""Password Strength Checker
Scenario: Build a password strength checker that ensures a password contains a mix of characters.
Use a set to keep track of character categories present in the password (e.g., lowercase, uppercase, digits, special characters).
Check if the password contains at least one character from each required category.
Display a message indicating whether the password is strong or weak.
Bonus: Suggest missing character categories to improve password strength."""



password = input("Create your password:")
print(password)

def check_password_strength(password):
    character_categories = set()
    if any(c.islower() for c in password):
        character_categories.add("lowercase")
    if any(c.isupper() for c in password):
        character_categories.add("uppercase")
    if any(c.isdigit() for c in password):
        character_categories.add("digits")
    if any(c in "!@#$%^&*()" for c in password):  # Example special characters
        character_categories.add("special")

    required_categories = {"lowercase", "uppercase", "digits", "special"}
    missing_categories = required_categories - character_categories

    if len(missing_categories) == 0:
        return "Strong password!"
    else:
        return f"Weak password. Consider adding: {', '.join(missing_categories)}"

# Example usage
print(check_password_strength("Password123"))  
print(check_password_strength("password"))  
print(check_password_strength("PASSWORD"))  