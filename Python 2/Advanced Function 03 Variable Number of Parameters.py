# Author: Brian Candido
# Purpose: Python variable parameter values function:

# put a * in front of the variable to denote a tuple or
# variable number of parms:

# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
#
# This way the function will receive a tuple of arguments,
# and can access the items accordingly:



def my_variable_parameters_function(*sKids):
  print("All kids: ", sKids)
  iChildCount = 1
  for sName in sKids:
    print(iChildCount, sName)
    iChildCount += 1



def main():

  # My own family: 
  my_variable_parameters_function("Daniel", "Joseph", "Moose")

  # My siblings:
  my_variable_parameters_function("Mathias", "Lauryn", "Bradeis", "Karon", "Michel", "Lizabeth", "Brian")

  

main()



