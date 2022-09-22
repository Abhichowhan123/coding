for j in range(int(input())):
    a,b = map(int,input().split())
    n = 0
    for i in range(1,b+1):
        if (a%i>n):
            n=a%i
    print(n)
