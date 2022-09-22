n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# A = [2,4,6,8,9,10,12]
# B = [ 4,6,8,9,10,12]
l = 0
h = len(A)-1
while l<=h:
    m = (l+h)//2
    if m==len(B)-1 and B[m]==A[m]:
        print(len(A)-1)
        break
    if m==0 and  A[m]!=B[m]:
        print(0)
        break
    if A[m]==B[m] and A[m+1]!=B[m+1]:
        print(m+1)
        break
    elif A[m]!=B[m] and A[m-1]==B[m-1]:
        print(m)
        break
    elif A[m]==B[m]:
        l=m+1
    elif A[m]!=B[m]:
        h=m-1
