"""A = []
k = 0
m = 12
n = int(input())
while m != 0:
    a = n % 2
    A.append(a)
    n = int(n/2)
    m-=1
for i in range(len(A)):
    if (A[i] == 1):
        k += 1
print(k)"""

A = [1,2,4,8,16,32,64,128,256,512,1024,2048]

tes =int(input())
while (tes!=0):
    i = 11
    j = -1
    count = 0
    n = int(input())
    while(n!=0):
        if (A[i] > n ):
            i -= 1
        else:
            n = n-A[i]
            count += 1
    print(count)
    tes-=1