from NumerologyLifePathDetails import NumerologyLifePathDetails

def main():
    name = input("Enter your full name: ")
    dob = input("Enter your date of birth (mm-dd-yyyy): ")

    # Create an instance of NumerologyLifePathDetails
    numerology_details = NumerologyLifePathDetails(name, dob)

    # Display the results
    print("Name:", numerology_details.getName())
    print("Date of Birth:", numerology_details.getBirthdate())
    print("Life Path Number:", numerology_details.getLifePath())
    print("Life Path Description:", numerology_details.getLifePathDescription())


main()
