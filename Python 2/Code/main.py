# Scott Minalga
# Let hope this works


def main():
    # Initialize a variable to keep track of the password validity
    valid = True

    # Step 1: Prompt the user for their First and Last name and store in a variable called sName.
    sName = input("Enter your First and Last name: ")

    # Step 2: Prompt the user for their desired password and store in a variable called sPassword.
    sPassword = input("Enter your desired password: ")

    # Step 3: Extract the first initial from the first name and the first initial from the last name from sName.
    sInitials = sName.split()[0][0] + sName.split()[1][0]
    sInitials = sInitials.upper()

    # Step 4: Ensure the password length is between 8 and 12 characters.
    if not (8 <= len(sPassword) <= 12):
        print("Password must be between 8 and 12 characters.")
        valid = False  # Set valid to False as this condition is not met

    # Step 5: Ensure the password does not start with Pass or pass.
    if sPassword.startswith('Pass') or sPassword.startswith('pass'):
        print("Password can't start with Pass.")
        valid = False

    # Step 6: Ensure the password contains at least one uppercase letter.
    if not any(char.isupper() for char in sPassword):
        print("Password must contain at least 1 uppercase letter.")
        valid = False

    # Step 7: Ensure the password contains at least one lowercase letter.
    if not any(char.islower() for char in sPassword):
        print("Password must contain at least 1 lowercase letter.")
        valid = False

    # Step 8: Ensure the password contains at least one number between 0 and 9.
    if not any(char.isdigit() for char in sPassword):
        print("Password must contain at least 1 number.")
        valid = False

    # Step 9: Ensure the password contains at least one of the special characters: ! @ # $ % ^.
    if not any(char in "!@#$%^" for char in sPassword):
        print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
        valid = False

    # Step 10: Ensure the password does not contain the value of sInitials.
    if sInitials.lower() in sPassword.lower():
        print("Password must not contain user initials.")
        valid = False

    # Step 11: Ensure no character is present more than once in the password.
    char_count = {}  # Dictionary to store counts of each character in the password.
    for char in sPassword:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1  # Incrementing the count of the character.
    repeating_chars = [char for char, count in char_count.items() if count > 1]  # Find repeating characters.
    if repeating_chars:
        print(f"These characters appear more than once: {', '.join(repeating_chars)}")
        valid = False

    # Step 12: If all checks are passed, print the success message, otherwise print invalid message.
    if valid:
        print("Password is valid and OK to use.")
    else:
        print("Password is invalid.")


# Ensure the main function is called.
if __name__ == '__main__':
    main()
