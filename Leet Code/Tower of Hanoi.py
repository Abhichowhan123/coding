def tower(A,B,C,D):
    if D==1:
        print("Move disk 1 from rod",A,"to rod",B)
        return
    tower(A,C,B,D-1)
    print("Move disk",D,"from rod",A,"to rod",B)
    tower(C,B,A,D-1)


A = [1,2,3]
B = []
C = []
D = 3
tower("A","B","C",D)