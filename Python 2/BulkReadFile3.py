#Author:  Prof. Candido
#Purpose: Read file of Dog Names and Ages and calculate
#         their human equivalent.

import csv

nDOG_FIRST_YEAR  = 12
nDOG_OTHER_FIRST = 7.3

# This function get the Dogs Name and Ages
def getNamesFromFiles():
   
    with open('NamesAndAgeWithHeadings.txt', 'r') as f:
      reader = csv.reader(f)
      #The CSV Reader takes each "row" and makes a list of it:
      data = [row for row in reader][1:]  # Exclude header row
      
      return data
    
def main():

    # Get the Dog's Name and Ages...
    lstNames = getNamesFromFiles()
    iEntriesInList = len(lstNames)

    print(f"The list contains: {iEntriesInList} values.")

    # Process each dog's name and age and compute human age:
    for sRecord in lstNames:
        #sRecordNameAge = sRecord.split(',')
        sName = sRecord[0]
        fAge = float(sRecord[1])

        # Or do assignment this way:
        sName, fAge = sRecord[0] , float(sRecord[1])
        

        if fAge <= 1:
           fHumanAge = fAge * nDOG_FIRST_YEAR
        else:
           fHumanAge = (fAge - 1) * nDOG_OTHER_FIRST + nDOG_FIRST_YEAR

        print(f"{sName:10s} age is: {format(fAge,'5.2f')} human age equivalent is: {format(fHumanAge,'5.2f')} ")

main()
    
    
