def maximum(max,a,b):
    y = x = 0
    f = "?"
    for k in range(len(a)):
        if (a[y] == f) or (b[x] == f) or a[y] != b[x]:
            max += 1
            y += 1
            x += 1
        else:
            y += 1
            x += 1
    return max
def minimum(min,a,b):
    y = x = 0
    f = "?"
    for j in range(len(a)):
        if (a[y] == b[x]) or (a[y] == f) or (b[x] == f ) or (f ==a[y])or (f ==b[x]):
            y += 1
            x += 1
        else:
            min += 1
            y += 1
            x += 1
    return min

for i in range(int(input())):
    a = list(input())
    b = list(input())
    min = 0
    max = 0
    y = x = 0
    f ="?"
    r = maximum(max,a,b)
    s = minimum(min,a,b)
    print(s,r)