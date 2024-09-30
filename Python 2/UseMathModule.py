# Prof. Candido
# Sample using the math module:

import math

def main():
     # Ask for 2 int numbers and then find the smallest,largest, average and sum:
     iNumber1 = int(input("Enter an int for a Number 1: "))
     iNumber2 = int(input("Enter an int for a Number 2: "))
##
     print("Pow:", math.pow(iNumber1, iNumber2))
     
     fNumber1 = float(input("Enter a float for a Number 1: "))
     print("Round",   round(fNumber1)    )
     print("Round 2", round(fNumber1,2)  )
     
     fNumber1 = float(input("Enter a float for a Number 1: "))
     print("floor", math.floor(fNumber1))

     fNumber1 = float(input("Enter a float for a Number 1: "))
     print("ceil", math.ceil(fNumber1))



# Call the main() function:   
main()
