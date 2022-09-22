# for i in range(int(input())):
#     A1,A2 = list(map(int,input().split()))
#     B1, B2 = list(map(int, input().split()))
#     C1, C2 = list(map(int, input().split()))
#     ma =max((A1+A2),(B1+B2),(C1+C2))
#     print(ma)
for i in range(int(input())):
    A1,A2 = [int(x) for x in input().split()]
    B1, B2 = [int(x) for x in input().split()]
    C1, C2 = [int(x) for x in input().split()]
    a = (A1+A2)
    b=(B1+B2)
    c=(C1+C2)
    ma =max(a,b,c)
    print(ma)