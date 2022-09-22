for i in range(int(input())):
    n = int(input())
    count = 0
    for j in range(1,n+1):
        n=n-j
        if(n>=0):
            count+=1
        else:
            break
    print(count)