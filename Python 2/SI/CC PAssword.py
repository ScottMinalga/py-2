def main():
    # Ask user for name first and last
    sName = input("Please enter your first and last name: ")
    # Call GetInitials function and assign to variable
    sInitials = GetInitials(sName)
    # Call GetPassword function and assign to variable
    sValidPassword = GetPassword(sInitials)


# Function to slice out initials from first and last name
def GetInitials(sName):
    # split first and last name
    sName = sName.split()
    # pull first letter from each name and place in list
    sInitialsSplit = [name[0] for name in sName]
    # join list and assign
    sInitials = "".join(sInitialsSplit)
    # return Initials
    return sInitials


# Function to ask for a password from the user and validate
def GetPassword(sInitials):
    # Initiate checks to validate password
    chkLength = chkPass = chkUpper = chkLower = chkDigit = chkSpecChar = chkInitials = sPasswordValid = False
    chkCharCount = True

    # Enter loop to validate password
    while sPasswordValid == False:
        # Ask user for password
        sPassword = input("Please enter a password: ")
        # Test password length
        if len(sPassword) >= 8 and len(sPassword) <= 12:
            chkLength = True
        # Test to check if Password begins with "pass"
        if sPassword[:4].lower() != "pass":
            chkPass = True
        # Test password containing users initials
        if sPassword.lower().find(sInitials.lower()) == -1:
            chkInitials = True
        # Initiate character count dictionary
        sCharCount = dict()
        # Enter loop to check individual characters
        for i in sPassword:
            # Populate dictionary with characters
            sCharCounts = sPassword.count(i)
            sCharCount[i] = sCharCounts
            # Test for multiple characters in password
            if sCharCount.get(i) >= 2:
                chkCharCount = False
            # Test if password contains 1 upper case letter
            if i.isupper():
                chkUpper = True
            # Test if password contains 1 lower case letter
            elif i.islower():
                chkLower = True
            # Test if password contains 1 number
            elif i.isdigit():
                chkDigit = True
            # Test if password contains 1 special character
            elif i == "!" or i == "@" or i == "#" or i == "$" or i == "%" or i == "^":
                chkSpecChar = True
                # Check all validators for true and validate password
        if chkLength and chkPass and chkLower and chkUpper and chkDigit and chkSpecChar and chkInitials and chkCharCount:
            print("Password is valid and OK to use.")
            sPasswordValid = True
            return sPassword
        # Print all failing validators
        else:
            if not chkLength:
                print("Password must be between 8 and 12 characters.")
            if not chkPass:
                print("Password can’t start with Pass.")
            if not chkUpper:
                print("Password must contain at least 1 uppercase letter.")
            if not chkLower:
                print("Password must contain at least 1 lowercase letter.")
            if not chkDigit:
                print("Password must contain at least 1 number.")
            if not chkSpecChar:
                print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
            if not chkInitials:
                print("Password must not contain user initials.")
            if not chkCharCount:
                print("These characters appear more than once: ")
                for i in sCharCount:
                    if sCharCount.get(i) >= 2:
                        print(f"{i}: {sCharCount.get(i)} times")
        # Reset all validators to default
        chkLength = chkPass = chkUpper = chkLower = chkDigit = chkSpecChar = chkInitials = False
        chkCharCount = True


# Call to main
main()