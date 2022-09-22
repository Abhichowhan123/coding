
def repeating(l  ,h ):
    while l<=h:
        m=(l+h)//2
        if len(A)==2:
            return A[0]
        elif A[m]==m and A[m]==A[m-1]:
            return A[m]
        elif A[m]%2==0 and m%2!=0 or A[m]%2!=0 and m%2==0 :
            l=m+1
        elif A[m]==m and A[m]!=A[m-1]:
            h = m-1

n = int(input())
A= list(map(int,input().split()))
print(repeating(l = 0 ,h = len(A)-1))