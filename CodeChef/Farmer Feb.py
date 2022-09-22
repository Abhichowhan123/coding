def pri(n,d,A):
    v=0
    for i in range(0,n):
        count = 0
        for j in range(1, n):
            if n % j == 0:
                count += 1
                if count==2:
                    break
        if (count == 1):
            A.append(n)
            v += 1
        if (v == 2):
            break
        n+=1
for i in range(int(input())):
    A = []
    a,b=map(int,input().split())
    c = (a+b)
    d = c*2
    f = 0
    pri(c,d,A)
    for j in range(len(A)):
        if(c<A[j]):
            f = A[j]-c
            break
    print(f)

