n = int(input())
A = list(map(int,input().split()))
LHS =[]
RHS=[]
count1 = 0
count2 = 0
for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            LHS[count1] = (A[i]*A[j])+A[k]
            count1+=1

for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            if A[i]!=0:
                RHS[count2]=A[i]*(A[j]+A[k])
                count2+=1
RHS = sorted(RHS)
print(RHS)
print(LHS)