# file handling with open

file = open('./chapter2_err_excep_file_handling/text.txt', mode='r')

data = file.readlines() # readlines for all lines. readline when the file has just one line,read only the first one.

print("\nOpen", data)

file.close()


# file handling with "with"

with open('./chapter2_err_excep_file_handling/text.txt', mode='r') as file:
    data = file.readline() # This time just for the first line
    print("\nWith", data)