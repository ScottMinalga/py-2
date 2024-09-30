# Code to demonstrate working of 
# Functions as dictionary values
# Using With parameters 

#https://www.geeksforgeeks.org/python-store-function-as-dictionary-value/

def avg_keys(t1, t2):
    return (t1 + t2) / 2
  
# Mostly works - Do not need Test1 and Test1 since pass it on line 18
dict_student_grades = {
             "mkc": {"code": avg_keys, "Test1" : 100, "Test2" : 95},
             "blc": {"code": avg_keys, "Test1" : 90, "Test2" : 80}
            }

# Dynamic add of entry:
dict_student_grades["bentz"] = {"code": avg_keys, "Test1" : 80, "Test2" : 70}

# Output using loop:
#for  Entry in  test_dict.values():
for  key, Entry in  dict_student_grades.items():

    print(key,Entry )
    res = Entry['code'](10, 34)
    print(res)

    print("alt: ", Entry['code'](Entry['Test1'], Entry['Test2']) )

