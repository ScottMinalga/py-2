# This program demonstrates how to read data from a file and
# includes code to make sure the numeric values are in fact a number before
# add the first name and salary to a lists.


import matplotlib.pyplot as plt

###############################################################
# main():                                                     #
# Starting point                                              #
###############################################################
def main():

    # Get the data from the file.  Notice how you can
    # return a list from the function.  In this example the
    # function returns 2 lists:
    sFirstNamesList, fSalaryList = readDataFromFile()

    # Build the bar graph
    plt.bar(sFirstNamesList, fSalaryList)

    # Add a title.
    plt.title('Bar Graph Employee Salary by Prof. C')

    plt.grid(True)

    # Display the line graph.
    plt.show()


###############################################################
# readDataType():                                             #
# This function will take in a string and determine if it is  #
# -int                                                        #
# -float                                                      #
# -string                                                     #
###############################################################
def getDataType(nToCheck):
    try:
        # if both the same the number is an int
        if int(nToCheck) == float(nToCheck):
            return 'int'
    except:
       # if not int check to see if it is a float:
       try:
            float(nToCheck)
            return 'float'
       # it must a string: 
       except:
            return 'str'

###############################################################
# readDataFromFile():                                         #
# Read the data from the file and place First Name and Salary #
# into a list and then return them:                           #
###############################################################
def readDataFromFile():

    sFirstNameFromFileList = []
    sLastNameFromFileList = []
    fSalaryFromFileList = []

    fileInput = open('FileReadSampleSplit.txt', 'r')

    # Read the record and remove the new line character from the end:
    recInput = fileInput.readline()
    recInput = recInput.rstrip('\n')
    
    # Process each record in the file until there are no more:
    while recInput != '' :
        iBegin = 0
        iEnd = 0
        sFirstName = ""
        sLastName= ""
        fSalary=0.0

        # Extract/Parse/Substring/Slice each fields
        sFields = recInput.split(',')

        print(sFields[0] )
        print(sFields[1])
        print(sFields[2])
        
        # get first name:
        sFirstNameFromFileList.append(sFields[0])

      
        #Get Salary from after the last , and to the end of the string contents:
        # Convert it from string to a float:
        sDataType = getDataType(sFields[2])
        if sDataType == 'int' or sDataType == 'float':
           fSalary = float(sFields[2])
        else:
            fSalary = 0
            
        fSalaryFromFileList.append(fSalary)
        
    
        # Read next record and remove the new line character from the end:
        recInput = fileInput.readline()
        recInput = recInput.rstrip('\n')

    # Close the file after exiting the loops:
    fileInput.close()

    # Return both lists to the main function:
    return sFirstNameFromFileList, fSalaryFromFileList

# Program starting point:
main()
