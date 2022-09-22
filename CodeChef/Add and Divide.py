for i in range(int(input())):
    a,b =map(int,input().split())
    x = 0
    count = 0
    while x!=1:
        x=x+a
        if x % b == 0:
            while x!=1:

                x=int(x/b)
                if x==1:
                    print("YES")
                else:
                    print("NO")