for i in range(int(input())):
    n = int(input())
    h = list(map(int,input().split()))
    if n%2 ==0:
        print("no")
        break
    mid = (len(h)//2)+1
    A = []
    a = 1
    for j in range(mid):

        A.append(a)
        a+=1
    b=mid
    for k in range(mid-1):
        b-=1
        A.append(b)
    if A ==h:
        print("yes")
    else:
        print("no")