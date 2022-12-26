# Example 1
class A:
    def a(self):
        return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):
    pass

# Driver code
c = C()
print(c.a())   # Function inside B


# Example 2

class D:
    def b(self):
        return "Function inside D"

class E:
    def b(self):
        return "Function inside E"

class F(D, E):
    def b(self):
        return "Function inside F"
    pass

class G(F):
    pass

d = D()
print(d.b())  # Function inside D



# Example 3

class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())

# OUTPUT: Function inside E
# [<class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

