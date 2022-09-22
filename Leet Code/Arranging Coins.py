import math
n = 1804289383
a = 0
for i in range(n//2):
    a += i
    if a>n:
        print(i-1)
        break
