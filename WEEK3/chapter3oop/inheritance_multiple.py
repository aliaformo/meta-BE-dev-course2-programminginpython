class A:
    a = 1



class B:
    b = 2
    

class C(A,B):
    pass


c = C()

print(c.a, c.b)  #   1         2


# Multi-level inheritance
class D:
    d = 1

class E(D):
    d = 2

class F(E):
    pass

f = F()
print(f.d)  # The output is 2 because F derives from the immediate super class of F, and that's E.


# Built-in functions

# issubclass()

# issubclass(class A, class B)

print(issubclass(A,B))  # False 
print(issubclass(B,A))  # True


# isinstance() that determines if some object is an instance of some class.

class A:
    pass

class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,B))


# super() function helps drive the flow of the code execution. It helps in managing or determining the control of from where I can draw the values of my desired functions and variables.

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()