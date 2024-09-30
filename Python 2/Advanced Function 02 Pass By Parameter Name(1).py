# Author: Brian Candido
# Purpose: Python Pass By Parameter Name:


def ThreeChildrenNameFunction(sChild1, sChild2, sChild3):
  print("Child 1 is:", sChild1,sep='|')
  print("Child 2 is:", sChild2,sep='|')
  print("Child 3 is:", sChild3,sep='|')
  


def main():

  # Pass by position:
  ThreeChildrenNameFunction("Daniel", "Joseph", "Moose")
  
  # Pass by parameter name: 
  ThreeChildrenNameFunction(sChild3 = "Moose", sChild1 = "Daniel", sChild2 = "Joseph")

main()



