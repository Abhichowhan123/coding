def repeating(l,h ):
    while l<=h:
        m=(l+h)//2
        if len(A)==1:
            return A[0]
        elif A[len(A)-1]!= A[len(A)-2] :
            return A[len(A)-1]
        elif A[0]!= A[1] :
            return A[0]

        elif A[m]!=A[m-1] and  A[m]!=A[m+1]:
            return A[m]
        elif m==len(A)-1 and (A[m]==A[m-1] and m%2!=0 and (m-1)%2==0):
            l = m + 1
        elif m==0 and (A[m]==A[m+1] and m%2!=0 and (m+1)%2==0):
            h = m - 1
        elif (A[m]==A[m-1] and m%2!=0 and (m-1)%2==0) or  (A[m]==A[m+1] and m%2==0 and (m+1)%2!=0):
            l = m+1
        elif(A[m]==A[m-1] and m%2==0 and (m-1)%2!=0) or (A[m]==A[m+1] and m%2!=0 and (m+1)%2==0):
            h=m-1

n = int(input())
A= list(map(int,input().split()))
print(repeating(l = 0 ,h = len(A)-1))