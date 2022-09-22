for  i in range(int(input())):
    A,B = map(int,input().split())
    if A>0 and B>0:
        print("Solution")
    elif B <=0 and A>0:
        print("Solid")
    elif A<=0 and B>0:

        print("Liquid")