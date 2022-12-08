# Readline. The readline function returns a single line.

with open("testing.txt", "r") as file:
    print("Just the first line:", file.readline())
    
# Output: Just the first line: This is the first line.


# readline(n) reads only an specific number of characters on a line.
with open("testing.txt", "r") as file:
    print("The first 10 characters:", file.readline(10)) 

# Output: The first 10 characters: This is th


# realines() method reads the entire content of a file and returns it in an ordered list.
# This allows you to iterate over the list or pick out specific lines based on a condition. 
# If for example, you have a file with four lines of texts and pass a length condition.

with open("testing.txt", "r") as file:
    lines = file.readlines()
    print("len:", len(lines))
    
    for line in lines:
        print(line)
        
        

# Examples

with open("sample.txt", 'r') as file:
    print(file.read())
    
    
with open("sample.txt", 'r') as file:
    print(file.read(44))
    
    
with open("sample.txt", 'r') as file:
    print(file.readline())
    
    
with open('sample.txt', 'r') as file:
    print(file.readlines())
    
    
# Lastly, because it's a list, I can assign it to a variable. I can say data equals file.readlines. Then I can write a for loop for x in data. I print the value of x, and then the list items are printed out line by line. When you use the with open and you get as file, it returns a list by default. I can just change the for loop so that it points to the file variable. 

with open('sample.txt', 'r') as file:
    data = file.readlines()
    
    for line in data:
        print(line)