# import the random module

import random
# Now I can use the random module's choice() function: random.choice().

# Storing file contents in data structures

f = open('petnames.txt', 'r')
f_content = f.read()
# get the f_content variable into a list
f_content_list = f_content.split('\n')
print(random.choice(f_content_list))



# If I had multiple files in my folder, I could allow myself to pick a file from which to read in a list of names.

import random
f_name = input('Type the file name: ') # input the file name of your interest
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))

# Output: Type the file name: petnames.txt
#Ace