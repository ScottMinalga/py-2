# Author: Brian Candido
# Purpose: Python Default Functions values:


def my_default_function(sCountry = "USA"):
  print("I am from " + sCountry)


def main():

  my_default_function("Sweden")
  my_default_function("India")
  my_default_function()
  my_default_function("Brazil") 

main()



