'''
Author: Dylan D. Hess
Purpose: Password validator
Date: 03FEB2024
Lets not forget P.E.M.D.A.S
Parthenthes:()              Exponents: **               Modulus: %
Multiplication: *            Division:  / (floating)     Division: // (int)
Addition: +                  Subtraction: -

> greater than           >= greater than or equal to
< less than                <= less than or equal to
== equal to               != not equal to
if/or/and/not
while/for/try/except
function acornyms: PL=         Password Length validates the proper length of the password entered
                             VPNP=   Validate Password No Pass, verifying that the password entered doesnt start with pass
                               VPC=    Validate Password Case
                               VPN=    Validate Password Number
                             VPSC=    Validate Password Special Characters
                               VPNI=   Validate Password No Initials
                               CCO=    Check Character Occurance
                               GUN=    Get User Name
                               GNP=    Get New Password

'''


def PL(sPassword):
    return 8 <= len(sPassword) <= 12


def VPNP(sPassword):
    if sPassword.lower().startswith("pass"):
        return False
    return True


def VPC(sPassword):
    return any(char.isupper() for char in sPassword) and any(char.islower() for char in sPassword)


def VPN(sPassword):
    return any(char.isdigit() for char in sPassword)


def VPSC(sPassword):
    SpecialChars = "!@#$%^"
    return any(char in SpecialChars for char in sPassword)


def VPNI(sPassword, initials):
    for initial in initials:
        if initial.lower() in sPassword.lower():
            return False
    return True


def CCO(sPassword):
    sCharCount = {}
    sDuplicates = []
    for char in sPassword:
        sCharCount[char.lower()] = sCharCount.get(char.lower(), 0) + 1
    for char, count in sCharCount.items():
        if count > 1:
            sDuplicates.append((char, count))
    if sDuplicates:
        print(f"These characters appear more than once:")
        for char, count in sDuplicates:
            print(f"{char}: {count} occurrences")


def GUN():
    sFirstName = input("Please enter your First Name: ")
    sLastName = input("Please enter your Last Name:")
    return sFirstName, sLastName


def GNP():
    sPassword = input("Please enter your new password: ")
    return sPassword


def main():
    sFirstName, sLastName = GUN()
    sName = sFirstName + " " + sLastName

    sInitials = sFirstName[0] + sLastName[0].upper()

    while True:
        sPassword = GNP()

        if PL(sPassword) == False:
            print("Password must be between 8 and 12 characters. Please try again.")
        elif VPNP(sPassword):
            print("Password can’t start with Pass. Please try again.")
        elif VPC(sPassword):
            print("Password must contain at least 1 uppercase letter and 1 lowercase letter. Please try again.")
        elif VPN(sPassword):
            print("Password must contain at least 1 number. Please try again.")
        elif VPSC(sPassword):
            print("Password must contain at least 1 of these special characters: ! @ # $ % ^. Please try again.")
        elif VPNI(sPassword, sInitials):
            print("Password must not contain user initials. Please try again.")
        else:
            break

    CCO(sPassword)

    print("Password is valid and OK to use.")


main()