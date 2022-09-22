# checking one no is prime or not

import math
for j in range (int(input())):
    n = int(input())
    count = 0
    f = int(math.sqrt(n))
    for i in range (2,f+1):
        if n%i==0:
            count+=1
    if count==0:
        print("prime")
    else:
        print("not prime")

# finding prime no from 1 to n
"""import math
for i in range(int(input())):
    n = int(input())
    v = 0
    for j in range(2,n+1):
        f =int( math.sqrt(j))
        count = 0
        for k in range(2,f+1):
            if j%k==0:
                count+=1
        if count == 0:
            v+=1
    print(v)"""
#
# import math
# for i in range(int(input())):
#     n = int(input())
#     if n<2:
#         print("0")
#         break
#     for j in range(2,n+1):
#         f =int( math.sqrt(j))
#         count = 0
#         for k in range(2,f+1):
#             if j%k==0:
#                 count+=1
#         if count == 0:
#             print(j,end=" ")


