
my_tuple = (1, 'strings', 3, 4.5, True, 3)

print(my_tuple[1])

print(type(my_tuple))

print(my_tuple.count(3))

print(my_tuple.index(4.5))

# tuple are iterable too

for i in my_tuple:
    print(my_tuple.index(i),i )
    
    
    
# tuples are immutable