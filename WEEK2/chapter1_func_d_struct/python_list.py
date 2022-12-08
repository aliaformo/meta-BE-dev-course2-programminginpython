
list1 = [1,2,3,4,5]
print(list1[3])

list2 = ['A', 'B', 'C']

print(*list2)

list3 = ['Hello', 7, True, 40.22]

print(list3, sep = ' ')

# ADDING

list4 = [1, [2,3,4], 5, 6]
# you can specify the index
list4.insert(len(list4), 7)

print(list4, sep = ' ')

list5 = [4, 9, 16, 25]
# append to the end
list5.append(36)

print(list5)


list6 = [1000, 900, 800, 700]
# extend a list too
list6.extend(list4) # or [1,2,3,4,5]
print(list6)


# REMOVING 

#POP
list7 = [7,6,8,0,5]
#specify the index other wise it removes the las element
list7.pop(0)
print(list7)

#DEL (in this case you should specify the index)
list8 = [23,58,46,95]
del list8[len(list8) - 1] # or any number inside the len of the list


# list iteration

for i in list8:
    print("value", i)
    
    
new_list = [1,2,3,4]
new_list.append(5)

print(new_list)