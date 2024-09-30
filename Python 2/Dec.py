# Author:    Prof. C

# Purpose:   Code that logs how long it takes to execute:
#            -How long to factorilize a number that is entered
#            -How long sum up all the number up to a entered number

# Challenge: Take this code and rewrote implement Python decorators that...
#            1.Identify what is duplicated between class to the 2
#              functions bc_factorial and bc_sum
#            2.Take what is common and place into a decorator called
#              decorate_prof_c_code and create a wrapper function
#              called wrapper() tht does this...
#              2.1 Determine what happens before the bc_factorial or
#                  bc_sum is called
#              2.2 Call the bc_factorial or bc_sum function
#              2.3 Determine what happens after the bc_factorial or
#                  bc_sum is called

from datetime import datetime


# Prof C. code to factorialize:
# I know we can use:
# import math and math.factorial(nNumber)
# but I want to use my own code:
def bc_factorial(nNumber):
    iFactorial = 1

    for iCount in range(1, nNumber + 1):
        iFactorial *= iCount

    return iFactorial


# Prof C. code to sum numbers from 1 up to
# and including nNumber:
def bc_sum_numbers(nNumber):
    iSum = 0
    for iCount in range(1, nNumber + 1):
        iSum += iCount

    return iSum


def main():
    while True:

        try:
            nNumber = int(input("Enter a positive integer number to factorialize and sum (0 to exit): "))
        except:
            print("Enter an integer number to factorialize")
            continue

        if nNumber == 0:
            break
        elif nNumber < 0:
            continue

        ############################
        # Factorial Code Example:  #
        ############################

        # Get Start current date and time
        dtNow = datetime.now()
        print(f"Start of bc_factorial: {dtNow}")

        nResult = bc_factorial(nNumber)
        print(f"{nNumber}! is: {nResult:,}")

        # Get End current date and time
        dtNow2 = datetime.now()
        print(f"End of bc_factorial: {dtNow2}")

        # Get elapsed time between start and end:
        dtDiff = dtNow2 - dtNow
        print(f"Elapsed Time of bc_factorial: {dtDiff}\n\n")

        ##############################
        # Sum Numbers Code Example:  #
        ##############################

        # Get Start current date and time
        dtNow = datetime.now()
        print(f"Start of bc_sum_numbers: {dtNow}")

        nResult = bc_sum_numbers(nNumber)
        print(f"{nNumber} sum of all is: {nResult:,}")

        # Get End current date and time
        dtNow2 = datetime.now()
        print(f"End of bc_sum_numbers: {dtNow2}")

        # Get elapsed time between start and end:
        dtDiff = dtNow2 - dtNow
        print(f"Elapsed Time of bc_sum_numbers: {dtDiff}\n\n")


main()


def my_decorator(func):
    def wrapper():
        dtNow = datetime.now()
        print(f"Start of bc_factorial: {dtNow}")

        nResult = bc_factorial(nNumber)
        print(f"{nNumber}! is: {nResult:,}")

        # Get End current date and time
        dtNow2 = datetime.now()
        print(f"End of bc_factorial: {dtNow2}")

        # Get elapsed time between start and end:
        dtDiff = dtNow2 - dtNow
        print(f"Elapsed Time of bc_factorial: {dtDiff}\n\n")
