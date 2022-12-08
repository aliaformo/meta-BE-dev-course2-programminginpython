# 1 LOCAL SCOPE

def get_total(a,b):
    #local variable declared inside a function
    total = a + b
    return total

print("Get total", get_total(3,5)) # 8


# Accessing variable outside of the function:
# print(total)
# NameError: name 'total' is not defined


# 2. Enclosing scope
# Enclosing scope refers to a function inside another function or what is commonly called a nested function.

def get_total2(a,b):
    #enclosed variable declared inside a function
    total2 = a + b
    
    def double_it():
        #local variable
        double = total2*2
        print(double)
        
    double_it()
    #double variable will not be accessible
    print(double)
    
    return total2


# 3. Global scope

# global variable
special = 5

def get_total3(a,b):
    #enclosed scope variable declared inside a function
    total3 = a + b
    print("Special", special)
    
    def double_it():
        #local variable
        double = total3*2
        print("Spacial from local:", special)
        
    double_it()
    
    return total3

print("Total3", get_total3(7,9))


