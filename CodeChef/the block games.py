t = int(input())
for i in range(t):
    n = int(input())
    a = n
    c = 0
    while(n!=0):
        b = n%10
        c = c*10+b
        n = int(n/10)
    if (a==c):
        print("Wins")
    else:
        print("loses")