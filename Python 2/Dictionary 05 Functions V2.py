# Code to demonstrate working of 
# Functions as dictionary values
# Using With parameters 

#https://softwareengineering.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary

# make a dictionary of US states and major cities
cities = {'San Diego':'CA', 'New York':'NY', 'Detroit':'MI'}

# define a function to use on such a dictionary
def find_city (map, city):
    # does something, returns some value
    if city in map:
        return map[city]
    else:
        return "Not found"

# then add a final dict element that refers to the function
cities['_found'] = find_city

print( find_city (cities, 'New York') )

print(cities['_found'](cities, 'New York')) 
