greek = "alpha"
print(":Global declaration: " + greek, id(greek))

def b():
    greek = "beta"
    print("Inside local: " + greek, id(greek))
    
def c():
    greek = 'gamma'
    print("Enclosed: " + greek, id(greek))
    
c()
print("Inside local: End of local: " + greek, id(greek))

b()
print("Global after local execution: " + greek, id(greek))


# Local and global scope
country = "USA" # Global
print("Country name: " + country, id(country))
print(globals())  # Built in
print("------")

def d():
    country = "Germany" # Local
    print("Country name: " + country, id(country))
    print(locals())
    
d()
print("Country name:" + country, id(country))


# other example
def e():
    animal = "elephant"
    def f():
        nonlocal animal
        animal = 'giraffe'
        print('Inside nested function: ' + animal)
    print("Before calling function:" + animal)
    f()
    print("After nested functions:" + animal)
animal = 'camel'
e()
print("Global animal: " + animal, id(animal))