def add(A):
    i = 0
    a = A[i]+A[i+1]
    print(a)
def sort(A):

    for j in range(len(A)):
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
            else:
                i+=1
    add(A)
import readline

A = []
t = int(input())
for i in range(t):
    m = int(input())
    n = list(map(int,input().split()))
    A = n
    sort(A)

