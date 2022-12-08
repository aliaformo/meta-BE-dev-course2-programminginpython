
with open('newfile.txt', mode = 'w') as file:
    file.write("This is a new file created!") # for just a line
    
    

# # writelines

with open('another_new_file.txt', 'w' ) as file:
    file.writelines(['This is another new file created!', '\nThis is another line to be added!'])
    
    
    
# appending

# first I create a new file

with open('file_append.txt', 'w') as file:
    file.writelines(['\nTrying appending lines', '\nOne line', '\nAnother line'])
    
# after creating it ☝️ I append new lines just with 'a' 👇.
    
with open('file_append.txt', 'a') as file:
    file.writelines(['\nTrying appending lines', '\nOne line', '\nAnother line'])


# Handling exceptions when handling files

try:
    with open('sample/newfile.txt', 'r') as file:
        data = file.readlines()
        
except FileNotFoundError as e:
    print('EPIC ERROR!', e)
    

