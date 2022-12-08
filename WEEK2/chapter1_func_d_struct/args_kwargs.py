def sum_of(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_of(4, 5, 6))
print(sum_of(4, 5, 6, 7))


def sum_ofK(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
        
    return round(sum, 2)

print(sum_ofK(coffee=2.99, cake=4.55, juice=3.99))