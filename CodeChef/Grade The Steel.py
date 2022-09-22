t = int(input())
for i in range(t):
    H,C,T=map(float,input().split())
    if (H>50 and C<0.7 and T>5600):
        print("10")
    elif (H>50 and C<0.7 ):
        print("9")
    elif ( C<0.7 and T>5600):
        print("8")
    elif (H>50 and T>5600):
        print("7")
    elif (H>50 or C<0.7 or T>5600):
        print("6")
    else:
        print("5")