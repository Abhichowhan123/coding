for i in range(int(input())):
    m,x =[int(x) for x in input().split()]
    m-=1
    A= [x]*x
    A[0] =1
    for j in range(1,x):
        p = (m%(j+1))+1
        if A[i-1]<p:
            A[i] = A[i-1]
        else:
            A[i] = A[i-1]+1
    for k in range(x):
        print(A[k],end=" ")