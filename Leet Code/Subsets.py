
A = [1,2,3]
T = []
def rec(B,i):
    if i == len(A):
        T.append(B)
        return
    rec(B+[A[i]],i+1)
    rec(B,i+1)
B=[]
rec(B,i=0)
print(T)

