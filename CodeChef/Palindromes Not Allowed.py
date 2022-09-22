for i in range(int(input())):
    N = int(input())
    A= ""
    for j in range(N):
        if j%3==0:
            A+="a"
        if j % 3 == 1:
            A += "b"
        if j % 3 == 2:
            A += "c"
    print(A)
    continue

