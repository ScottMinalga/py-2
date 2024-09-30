# Authors Prof. C 
# Super Fantastic Students

class Rectangle:
    # First part of the code to set up and store
    # and protect/Encapsulate the length and width:
    def __init__(self, nWidth, nLength):
        self.__width = nWidth
        self.__length = nLength

# Use a single leading underscore only when you need to
# indicate that a variable, class, method, function,
# or module is intended for internal use within the containing module,
# class, or package.
# This is just a well-established naming convention. It's not a strict rule that Python enforces.

# _ means it is only for this class, but, Python will warn you
# __ means it is only for this class and NO warning is given

    # Code the "getters":
    def _getArea(self):
        return self.__width * self.__length
        
    def _getLength(self):
        return self.__length

    def _getPerimeter(self):
        return (self.__width * 2) + (self.__length * 2)

    def _getWidth(self):
        return self.__width

    # Code the "is-ers":
    def _isSquare(self):

        return self.__width == self.__length


    # Code the "setters":
    def _setLength(self, NewLength):
        self.__length = NewLength
    
    def _setWidth(self, NewWidth):
        self.__width = NewWidth

    # Since the methods/functions are hidden now create properties:

    # Syntax:
#    radius = property(
#                       fget=,
#                       fset=,
#                       fdel=,
#                       doc=""
#    )

#    fget is assigned the fuction when the property is used on the RIGHT
#         of the = sign or as parameter to a function()

#    fset is assigned the fuction when the property is used on the left
#         of a = sign

    # both a setter and getter:
    length = property(fget=_getLength,
                      fset=_setLength
                      )

    # both a setter and getter:                  
    width = property(fget=_getWidth,
                     fset=_setWidth,
                     )

    # getter only
    area = property(fget=_getArea)

    # getter only
    perimeter = property(fget=_getPerimeter)

    # getter only
    isSquare = property(fget=_isSquare)
        
    
