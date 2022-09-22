def counting(b):
    count = k = 0
    for j in range(1, b + 1):
        count += 1
        k = k + count
    return k

t = int(input())
for i in range(t):
    a, b = map(int, input().split())

    for l in range(a):
       b = counting(b)

    print(b)