#factorial using recursion

def fact(i):
    if i==0:
        return 1
    n=i*fact(i-1)
    return n
o=int(input("enter the no for factroial  "))
p=fact(o)
print(p)