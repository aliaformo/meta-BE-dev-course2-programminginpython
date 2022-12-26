menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    
    
# map function
map_coffee = map(find_coffee, menu)
print(map_coffee)  # <map object at 0x0000025745C97610>  map object

for i in map_coffee:
    print(i) 
    
# None
# None
# None
# cappuccino
# cortado
# None

# A map takes all objects in the list and allows you to apply a function to it


# filter function
filter_coffee = filter(find_coffee, menu)
print(filter_coffee) # <filter object at 0x000001B4F5306320>

for i in filter_coffee:
    print(i)

# cappuccino
# cortado

# A filter also allows you to take in all objects in the list and runs through a function but it creates a new list and only returns values where the evaluated function returns true.


