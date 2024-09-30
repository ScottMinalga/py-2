
# Declare a set: 
myset = {1, 2, 3, 4, 5}


thisset = {"apple", "banana", "cherry"}
print(thisset)



thisdict = dict.fromkeys(x, y)

print(myset)
print(len(myset))


# Add more once created:
myset.add(7)
myset.add(8)

print(myset)
print(len(myset))


# change the set: 
set2 = set([12,13,14])
myset.update(set2)

myset.update( set([20,21,22,23,24,25]) )

print(myset)
print(len(myset))

# Remove an entry:
myset.remove(25)
print(myset)
print(len(myset))


# Union Operators:

set3 = set([67,93,84,112,14])
print('Union', myset.union(set3) )

# Intersection Operators:
print('Intersection', myset.intersection(set3) )







