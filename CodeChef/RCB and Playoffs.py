for i in range(int(input())):
    X, Y, Z = map(int,input().split())
    if  X+(Z*1)>=Y or X+(Z*2)>=Y :
        print("YES")
    else:
        print("NO")