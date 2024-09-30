# Jacob Tuvek
# CIT-117-D01
# Password Validator

# 1 Promt for user name
sName = input("Enter Full Name: ")

# 2 promt user for their desired password
sPassword = input("Enter New Password: ")

# 3 Pull first letter from first and last name
sInitials = sName.title()[0] + sName[sName.find(" ") + 1]

# 4 password length check
if len(sPassword) < 8 and len(sPassword) > 12:
    print("Password must be between 8 and 12 characters")
else:
    False

# 5 make sure password does not contain "pass or Pass"
if sPassword.lower().startswith("pass"):
    print("Password cannot start with pass")
else:
    False


# 6 check for at least one capital
def UpperCase(sPassword):
    for sCharacter in sPassword:
        return True if sCharacter.isupper() else False


# 7 check for at least one lowercase
def LowerCase(spassword):
    for sCharacter in sPassword:
        return True if sCharacter.islower() else False


# 8 make sure password contains at least one number between 1-9
def NumericCheck(sPassword):
    for sNumber in sPassword:
        return True if sPassword.isalpha() else False


# 9 make sure special character is included
def SpecialCharacter(sPassword):
    for sSpecial in sPassword:
        return True if sPassword.isalnum() else False


# 10 No initials of user wanted in password
def NoInitials(sPassword):
    for sInitial in sPassword:
        return True if sPassword.find(sInitials.lower()[0]) != -1 or sPassword.find(
            sInitials.upper()[0]) != -1 else False


# 11 dictionary function to look for multiple characters
def NoDuplicates(sPassword):
    dictPass = {i: sPassword.count(i) for i in sPassword}
    for key in dictPass:
        if dictPass[key] > 1:
            return True
        print(" These characters appear more than once:", dictPass[key])


# main function
def main():
    # calling UpperCase function
    if UpperCase(sPassword) == False:
        print("Password must contain at least 1 uppercase letter")

    # calling lowecase function
    if LowerCase(sPassword) == False:
        print("Password must contain at least 1 lowercase letter")

    # calling NumericCheck function
    if NumericCheck(sPassword) == True:
        print("Password must contain at least 1 number")

    # calling SpecialCharacter function
    if SpecialCharacter(sPassword) == True:
        print("Password must contain at least 1 of these special characters! @ # $ % ^")

    # calling NoInitials function
    if NoInitials(sPassword) == True:
        print("Password must not contain user initials.")

    # calling NoDuplicates Function
    NoDuplicates(sPassword.lower())


# 12 if pass all requirements password good to use


main()