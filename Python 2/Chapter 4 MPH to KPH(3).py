# Prof. Candido
# Chapter 4 Loops - MPH to KPH

fCONVERSION_FACTOR = 0.6214

# Using a for loop:
print('\n\nMPH to KPH using a for:')

for iSpeed in range(5, 151, 5): 
    fKiloMetersSpeed = iSpeed / fCONVERSION_FACTOR
    print(iSpeed, '\t', format(fKiloMetersSpeed, '.0f') ) 

# Using a while loop:
print('\n\nMPH to KPH using a while:')

iSpeed = 5

while iSpeed <= 150 : 
    fKiloMetersSpeed = iSpeed / fCONVERSION_FACTOR
    print(iSpeed, '\t', format(fKiloMetersSpeed, '.0f') )
    iSpeed += 5



