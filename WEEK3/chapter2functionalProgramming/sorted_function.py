# Sorted function

coffees = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano', 'Decaf']

print(sorted(coffees))

# ['Americano', 'Cappuccino', 'Decaf', 'Espresso', 'Latte', 'Macchiato']


def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse, coffees)

print('reverse coffees', reversed_coffees)

for i in reversed_coffees:
    print(i)
    

