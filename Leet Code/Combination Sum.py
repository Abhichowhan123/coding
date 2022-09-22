A = [2,3,5]
B = []
def cobbination(i,tar,T):
    if tar<0:
        return
    if tar ==0:
        if T not in B :
            B.append(T)
        return
    for j in range(i,len(A)):
        cobbination(j,tar-A[j],T+[A[j]])
        cobbination(j+1,tar-A[j],T+[A[j]])
i = 0
tar =8
T = []
cobbination(i,tar,T)
print(B)
