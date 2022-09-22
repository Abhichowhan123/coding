def gcd(w,x):
    a = max(w, x)
    b = min(w, x)
    if (b == 0):
        print(a)
    while (a % b != 0):
        tem = a
        a = b
        b = tem % b
    return b
for r in range(int(input())):
    w, x = map(int, input().split())
    print(gcd(w,x),(w*x)//gcd(w,x))

