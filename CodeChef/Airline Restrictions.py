for i in  range(int(input())):
    A,B,C,D,E=map(int,input().split())
    if 1<=A<=10 and 1<=B<=10 and 1<=C<=10 and 15<=D<=20 and 5<=E<=10:

        if (A+B)<=D and C<=E or  (B+C)<=D and A<=E or (A+C)<=D and B<=E:
            print("YES")
        else:
            print("NO")