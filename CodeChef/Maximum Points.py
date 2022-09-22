for i in range(int(input())):
    A = list(map(int,input().split()))
    X= list(map(int, input().split()))
    time = 240
    ma = 0
    for j in range(3):
        if X[j]>ma:
            ma = X[j]
