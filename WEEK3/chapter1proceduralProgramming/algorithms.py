str = 'racecar'

def check_palindrome(word):
    
    if word == word[::-1]:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"
    

print(check_palindrome(str))


# ALGORITHMS

# Recursion
# Recursion refers to a method or a function that will call itself. It is used to resolve problems by breaking the problem down into sub-problems. Let us take a look at some of the most popular types of recursive algorithms.

# Divide and conquer
# This consists of two parts. The first is breaking the problem down into smaller sub-problems and the second is solving the final solution.

# Dynamic programming
# This is mainly used for optimization problems. It is similar to the divide and conquer algorithm in that it splits the problems into sub-problems.

# Greedy algorithm
# This one finds the best solution in each and every step instead of approaching optimization in a global way.