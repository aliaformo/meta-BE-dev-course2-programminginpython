
# declaring a dict

my_d = {}
print("my_d type", type(my_d))

my_d = {1: 'Test', 'Name': 'Jim'}
print(my_d)
print(my_d[1])

my_d[2] = 'Test2'
print(my_d)

# ITERATING

#This only iterates over the keys
for i in my_d:
    print(i)

# Iterating over both the keys and the values

for key, value in my_d.items():
    print(key, ":", value)


sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
print(sample_dict[1])
print(sample_dict)

sample_dict[2] = 'Mint Tea'
print(sample_dict) # {1: 'Coffee', 2: 'Mint Tea', 3: 'Juice'}


# deleting elements

del sample_dict[3]
print(sample_dict) # {1: 'Coffee', 2: 'Mint Tea'}
