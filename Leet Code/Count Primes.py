import math

n = 50
A =  [True]*(n+1)
if n<=2:
    print(1)
else:
    count = 0
    A[0] = A[1] = False
    f = math.ceil(math.sqrt(n))
    for i in range(2,n):
        if A[i]==True:
            count+=1
            for j in range(i*2,n+1,i):
                # if j%i==0:
                A[j] = False

    print(count)