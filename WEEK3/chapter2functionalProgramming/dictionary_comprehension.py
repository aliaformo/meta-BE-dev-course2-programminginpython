# The syntax for dictionary comprehension is:
# dict = { key:value for key, value in <sequence> if <condition> } 
# Dictionary comprehension takes one or two lists as input and creates a dictionary out of it. 

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Using range():  {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}


# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]


# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using one input list to create dict:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}



# Note how in case of using two lists, the format it follows is: 
# new_dict ={key:value for (key, value) in zip(list1, list2)}


# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

# Using two lists:  {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


# When the two lists are of unequal length, the length of the shorter list is the length of the dictionary.