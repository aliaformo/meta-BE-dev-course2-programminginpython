# also very similar to lists with the variation of using curved brackets instead of square brackets. They are also more memory efficient as compared to list comprehensions. 

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")
    
    
    
# <generator object <genexpr> at 0x102a87d60> 
# <class 'generator'> 
# 2 3 5 7 11 13 17 19 23 29 31 


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
    return numbers < 50

small = list(map(lesser, numbers))
print(small)