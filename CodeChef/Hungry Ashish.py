for i in range(int(input())):
    X,Y,Z = list(map(int,input().split()))
    if X>=Y:
        print("PIZZA")
        continue
    elif X>=Z:
        print("BURGER")
        continue
    else:
        print("NOTHING")
        continue