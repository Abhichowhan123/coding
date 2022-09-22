# A = [[1,5,9],
#      [10,11,13],
#       [12,13,15]]
# k =1
# n = 3
# 3
# 1 5 9
# 10 11 13
# 12 13 15
n = int(input())
A  = []
for i in range(n):
    B = list(map(int,input().split()))
    A.append(B)
k = int(input())
min  = 99999
max = 0
for i in range(len(A)):
    if min>A[i][0]:
        min =A[i][0]
    for j in range(1):
        if max< A[i][n-1]:
            max=A[i][n-1]
def fun(x):
    count = 0
    for i in range(len(A)):
        j=0
        while(j<=len(A[0])-1):
            if A[i][j]<=x :
                count+=1
            j+=1
    return count
l = min
h = max
while(l<=h):
    m = (l+h)//2
    count1 = fun(m)
    if count1<k:
        l=m+1
    elif count1>k:
        h = m-1
    else:
        count2=fun(m-1)
        if count2<k:
            # o = -1
            # while(m<=len(A)):
            #     o+=1
            #     m = m-len(A)
            print(m)
            break
        else:
            h = m-1

