# slice function
# str[start:stop:step] extended slice syntax

trial = "reversal"
new_trial = trial[::-1]
print(new_trial) # lasrever    In summary, the entire string is traversed from right to left, one index position at a time. 


# using recursion

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
str = 'reversal'
reverse = string_reverse(str)
print(reverse)  # lasrever


