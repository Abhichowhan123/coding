# n = int(input())
# A = list(map(int,input().split()))
# k = int(input())
A = [2,7,11,15]
k  =13
l = 0
h = len(A)-1
while(l<=h):
    m = (l+h)//2
    if A[l] + A[h] == k or A[0] + A[h] == k or A[l] + A[len(A)-1] == k:
        print(l+1, h+1)
        break
    if A[l]+A[h]>k or A[m]>k:
        h = m
    elif A[l]+A[h]<k :
        l = m
