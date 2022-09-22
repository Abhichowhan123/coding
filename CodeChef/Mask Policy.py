for i in range(int(input())):
    N,A= list(map(int,input().split()))
    if N == A:
        print("0")
        continue
    if N-A <=A:
        print(N-A)
        continue
    if  N-A >A:
        print(A)
        continue

