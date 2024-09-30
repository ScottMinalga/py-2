# Author: Prof C.

import RectangleWithProperties

def main():

    iWidth = int( input("Enter Width: "))
    iLength = int( input("Enter Length: "))
    
    myRect = RectangleWithProperties.Rectangle(iWidth,iLength)

    #No need for getters!

    print(f"Length is: {myRect.length} ")
    print(f"Width is: {myRect.width} ")
    
    print("Area: ", myRect.area )
    print("Perimeter: ", myRect.perimeter )
    print("Square: ", myRect.isSquare )


    # Now change them by using the setter
    print("\n\n")
    myRect.length = 20
    print(f"Length is: {myRect.length} ")
    myRect.width = 14
    print(f"Length is: {myRect.width} ")
    
    print("Area: ", myRect.area )
    print("Perimeter: ", myRect.perimeter )
    print("Square: ", myRect.isSquare )


main()
