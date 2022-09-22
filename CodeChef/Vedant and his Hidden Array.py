for i in range(int(input())):
    N,A = [int(x) for x in input().split()]
    if N==1:
        if (A%2==0):
            print("Even")
        else:
            print("Odd")
        continue
    if A%2==1:
        if N%2==0:
            print("Even")
        else:
            print("Odd")

    else:
        print("Impossible")