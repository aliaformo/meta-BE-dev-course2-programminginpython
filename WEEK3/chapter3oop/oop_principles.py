# Encapsulation
# self._a is a protected member and can be accessed by the class and its subclasses.


class Alpha:
    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’
        
        

# Polymorphism
# Polymorphism refers to something that can have many forms. In this case, a given object. Everything in Python is inherently an object, so, it can be an operator, method or any object of some class.

string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3
print(new_str, new_num, new_sequence)  # polypolypoly 21 [1, 2, 3, 1, 2, 3, 1, 2, 3]

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence)) # 4   3 



# Inheritance

class Parent:
    # Members of the parent class
    pass

class Child(Parent):
    # Inherited members from parent class
    # Additional members of the child class
    pass


# Abstraction

# it can be seen both as a means for hiding important information as well as unnecessary information in a block of code. The core of abstraction is the implementation of something called abstract classes and methods, which can be implemented by inheriting from something called the abc module, abstract base class. It is first imported and then used as a parent class for some class that becomes an abstract class. 

# from abc import ABC, 

# class ClassName(ABC):
    pass