import math

print("Importing the math module")

root = math.sqrt(9)
print(root)  # 3.0

# prevent overloading the interpreter by importing the entire math module
from math import sqrt

root1 = sqrt(4)
print(root1)  # 2.0

# Alias
import math as m
cosine = m.cos(0)
print(cosine) # 1.0

# alias and not overloading
from math import factorial as f

factorial_10 = f(10)
print(factorial_10) # 3628800


# several 

from math import factorial, sqrt, log10
x = log10(50)
print(x)  # 1.6989700043360187

# importing all functions from math
from math import *