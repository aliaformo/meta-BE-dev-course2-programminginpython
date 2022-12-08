
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("set", set_a)

set_a.add(10)

print("set add", set_a)

# Removing items

# Remove
# specify the data you want to remove NOT THE INDEX
set_a.remove(2)
print("set remove", set_a)


# Discard
# specify the data you want to discard too NOT THE INDEX
set_a.discard(10)
print("set discard", set_a)


# math operations

# union
set_b = {10, 20, 30, 40, 50, 60, 70, 8, 9}
print("union", set_a.union(set_b))

print("with |", set_a | set_b)

# intersection
# values that match set a and set b
print("intersect", set_a.intersection(set_b))
print("with &", set_a & set_b)

#difference
# elements that are only in set a and not in set b
print("difference", set_a.difference(set_b))
print("with -", set_a - set_b)


# symmetrical difference
print("symmetric_difference", set_a.symmetric_difference(set_b))
print("with carrot operator ^", set_a ^ set_b)



# set object is not subscriptable this means that the set is not a sequence, it doesn't contain an ordered index of all elements inside. 
# Unlike a list where I can print out content based on index

# print(set_a[0]) I'll get an error




