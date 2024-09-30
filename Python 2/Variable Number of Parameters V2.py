# Author: Brian Candido
# Purpose: Python variable parameter values function:

# put a ** in front of the variable to denote a dictionary that consists of:
# Parameter Name
# Parameter Value


def my_variable_parameters_function(**sKids):
  print("All kids: ", sKids)
  print('What is the Python data type:', type(sKids) ) 

  # Puts out the key only:  
  for sName in sKids:
    print(sName)

  print("\n\n")

  # Puts out the key AND value:  
  for sKey, sName in sKids.items():
    print(f"Key: {sKey} Value: {sName}")
  

def main():

  # My own family: 
  my_variable_parameters_function(Child1="Daniel", Child2="Joseph", Child3="Moose")

  # My siblings:
  my_variable_parameters_function(Child1="Mathias", Child2="Lauryn",   \
                                  Child3="Bradeis", Child4="Karon",    \
                                  Child5="Michel",  Child6="Lizabeth", \
                                  Child7="Brian")

  # Just Me :)
  my_variable_parameters_function(OnlyChild="Brian")

  # No One :{
  my_variable_parameters_function()

 
main()



