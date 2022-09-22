for i in range(int(input())):
    P,a,b,c,x,y = map(int,input().split())
    count = 0
    anar = (x*a)+b
    char = (y*a)+c

    if anar<=char:
        count = int(P/anar)

    if anar>=char:
        count = int(P/char)
    print(count)