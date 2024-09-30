# This program calculates Interest Rates within Number of Months

# How much do we have right now?
fInitial_Deposit = 0
fYearly_Int_Rate = 0
iNum_Of_Months = 0
fGoal_Amount = 0


while fInitial_Deposit <= 0:
    try:
        fInitial_Deposit = float(input('Enter Initial Deposit Amount: $ ')) # Must be positive numbers and no letters
        if fInitial_Deposit <= 0:
            print('ERROR: Value must be greater than zero.')
    except ValueError:
        print('ERROR: Value must be a whole number.')
# Everything works up here don't touch it.

while fYearly_Int_Rate <= 0:
    try:
        fYearly_Int_Rate = float(input('Enter Interest Rate: ')) # Must be positive numbers and no letters
        if fYearly_Int_Rate <= 0:
            print('ERROR: Value must be greater than zero.')
    except ValueError:
        print('ERROR: Value must be a whole number.')
# Everything works up here ALSO. Don't touch it.

while iNum_Of_Months <= 0:
    try:
        iNum_Of_Months = int(input('Number of Months: ')) # Must be positive numbers and no letters
        if iNum_Of_Months <= 0:
            print('ERROR: Value must be greater than zero.')
    except ValueError:
        print('ERROR: Value must be a whole number.')
#Everything works up here ALSO ALSO. Dont touch it. Don't even look at it.

while fGoal_Amount <= 0:
    try:
        fGoal_Amount = int(input('Goal Amount: $')) # Must be positive numbers and no letters
        if fGoal_Amount < 0:
            print('ERROR: Value must be greater than zero.')
        else:
            break # This works... ATM..
    except ValueError:
        print('ERROR: Value must be a whole number.')
#Final Input DONE and VERIFIED.. It all works. Move along.

# Turn Interest Rate into Monthly Interest Rate
fMonthly_Int_Rate = (fYearly_Int_Rate / 100) / 12 #Keep this math
# This works. Move along.

# Caluclate Number of Months with Compound Interest Rate
fCompound_Int = (fInitial_Deposit * fMonthly_Int_Rate) #New





# Output the Month Number and the Account Balance like example

 
i = 0 # Keep THIS 

while i <= iNum_Of_Months:
    i += 1 # Keep THIS!! 
    
    
    fAccount_Balance = fInitial_Deposit + fCompound_Int
    fInitial_Deposit += fCompound_Int

    fCompound_Int = fAccount_Balance * fMonthly_Int_Rate # New KEEP


    

    print(f"Month {i}: New Account Balance - ${fAccount_Balance:,.2f}") # Keep This

""" 
    print(f'Here is the Initial Deposit Amount: $ {fInitial_Deposit:,.2f}.')
    print('Here is the Interest Rate: ', fYearly_Int_Rate)
    print('Here is the Number Of Months: ', iNum_Of_Months)
    print('Here is the Goal Amount: $', fGoal_Amount)
    print('Here is the MONTHLY Interest Rate: ', fMonthly_Int_Rate) """
# Everything above this line works, dont touch it


###################################################
# NEW CODE BELOW THIS LINE:

# Initialize variables
fInitial_Deposit = 0
fYearly_Int_Rate = 0
iNum_Of_Months = 0
fGoal_Amount = 0

# Get user input for initial deposit, yearly interest rate, number of months, and goal amount







""" fMonthly_Int_Rate = (fYearly_Int_Rate / 100) / 12 # New

i = 0
#fAccount_Balance = fInitial_Deposit # Dont need

while fAccount_Balance <= fGoal_Amount: # Because we need to make it to our goal
    i += 1 # increasing number of months
    #fCompound_Int = fAccount_Balance * fMonthly_Int_Rate # Dont need
    fAccount_Balance += fCompound_Int
    

print(f"You will reach your goal of $ {fGoal_Amount:,.2f} in {i} months.") """ 

# NEW CODE ABOVE THIS LINE:
###################################################

## My Tests Below ## 
#print('PASS: Your code is working appropriately!')


