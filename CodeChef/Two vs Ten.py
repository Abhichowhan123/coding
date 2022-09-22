for i in range(int(input())):
    n = int(input())
    w = 0
    while (n % 10 != 0):
        if (n % 10 != 0):
            n = n * 2
            w += 1
            if n>10000000000:
                break
    if(n%10==0):
        print(w)
    else:
        print("-1")