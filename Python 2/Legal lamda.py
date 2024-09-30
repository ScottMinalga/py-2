



iflegal = lambda iAge: "legal" if iAge >= 21 else "not Legal"



def add(x,y):
    return x + y


add = lambda x, y: x + y
print(add(5, 3))  # Outputs: 8


square = lambda x: x * x
print(square(4))  # Outputs: 16


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Outputs: [1, 4, 9, 16, 25]


