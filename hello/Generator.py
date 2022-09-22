# Squar
"""using yield method"""

def topten():
    n =1
    while n<=10:
        sq = n*n
        yield sq
        n = n+1


A = topten()
for i in A:
    print(i)