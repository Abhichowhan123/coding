#lambda function
"""
f =lambda a,b:a+b
result = f(5,6)
print(result)"""

from functools import reduce


num = [98,14,56,2,5,1,5,56,88,45,565,4,2]

# filter
evens = list ( filter(lambda n:n%2==0,num))
print("selecting enenno forom list:- ",evens)

# map
doubles = list(map(lambda n:n*2,evens))
print("double of evens no :- ",doubles)


#reduce
sum = reduce(lambda a,b:a+b,doubles)
print("adding all values of doubles:-  ",sum)