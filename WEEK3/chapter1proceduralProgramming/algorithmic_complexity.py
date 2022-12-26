# Algorithmic complexity
# Algorithmic complexity is a measure of how long an algorithm will take to complete given the size of the input, or what is commonly called n or n times. The n represents the number of elements.  Algorithm complexity can be divided into two types:

# Time complexity refers to how long an algorithm takes to complete.

# Space complexity refers to the amount of memory needed to complete the algorithm.


def find_num(num):
    count = 0
    for i in range(100):
        if i == num:
            print('total iterations:', count)
            return i
        count +=1
        
find_num(97)  # 97



def find_number_log(target):
    iterations = 0
    x = range(100)
    left = 0
    right = len(x) -1
    
    while left <= right:
        iterations += 1
        middle = (left + right) // 2
        isNumber = x[middle]
        
        if target == isNumber:
            print('Iterations:', iterations)
            return middle
        elif target < isNumber:
            right = middle -1
        else:
            left = middle + 1
    return - 1
        
print(find_number_log(97))
        
        




