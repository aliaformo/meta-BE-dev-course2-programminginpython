
my_list = [1,2,3]

# not a pure function
def add_to_list(item):
    return my_list.append(item)    

add_to_list(4)
print(my_list)  # [1, 2, 3, 4]  The data has been manipulated at the global scope from inside the scope of the function


# not a pure function
def add_to_list(item):
    my_list.append(item) 
    return my_list   

new_list = add_to_list(4)
print(my_list) # [1, 2, 3, 4] The data has been manipulated at the global scope from inside the scope of the function
print(new_list) # [1, 2, 3, 4] # even though it's returning a new variable, it still has a reference to the my_list variable.


# not a pure function
def add_to_list(lst, item):
    lst.append(item)
    return lst
new_list = add_to_list(my_list, 4)
print(my_list) # [1, 2, 3, 4] The data has been manipulated at the global scope from inside the scope of the function
print(new_list) # [1, 2, 3, 4] # even though it's returning a new variable, it still has a reference to the my_list variable.


# PURE FUNCTION

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)
print(my_list) # [1, 2, 3]  # This function is now a pure function because it adds value to a list, but it doesn't manipulate the original list outside the function.
print(new_list) # [1, 2, 3, 4]
