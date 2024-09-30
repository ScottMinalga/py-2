# Author: Brian Candido
# Purpose: Annotations of Python data types as a parameter values:

#
# Function annotations are completely optional both for parameters
# and return value.

# Function annotations provide a way of associating various parts
# of a function with arbitrary python expressions at compile time.

# The PEP-3107 makes no attempt to introduce any kind of standard semantics,
# even for the built-in types.
# All this work left to the third-party libraries.


def sum_3_numbers(x: 'x should be an int or float' = 5, y: 'y should be an int or float y' = 6, z: int = 7) -> float:
    print(f"x value is: {x} and is this data type: {type(x)}")
    print(f"y value is: {y} and is this data type: {type(y)}")
    print(f"z value is: {z} and is this data type: {type(z)}")
    total = x + y + z
    return float(total)


def main():
    # ask the sum_3_numbers functions to share details about the
    # programmer comments/notes about the the parameters:
    print(sum_3_numbers.__annotations__)

    iSum = sum_3_numbers(1, 2, 3)
    print(f"The sum is: {iSum} and data type is: {type(iSum)} ")

    iSum = sum_3_numbers(1.0, 2, 3.0)
    print(f"The sum is: {iSum} and data type is: {type(iSum)} ")

    iSum = sum_3_numbers()
    print(f"The sum is: {iSum} and data type is: {type(iSum)} ")

    # Let us go into replit.com and use the annotations :)


main()






