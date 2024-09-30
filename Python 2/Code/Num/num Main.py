from Numerology import Numerology

def main():
    name = input("Enter your full name: ")
    dob = input("Enter your date of birth (mm/dd/yyyy): ")

    # Create an instance of Numerology
    numerology = Numerology(name, dob)

    # Display the results
    print("Name:", numerology.getName())
    print("Date of Birth:", numerology.getBirthdate())
    print("Life Path Number:", numerology.getLifePath())
    print("Attitude Number:", numerology.getAttitude())
    print("Birth Day Number:", numerology.getBirthDay())
    print("Personality Number:", numerology.getPersonality())
    print("Power Name Number:", numerology.getPowerName())
    print("Soul Number:", numerology.getSoulNumber())

main()
