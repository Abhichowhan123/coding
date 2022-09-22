for i in range(int(input())):
    N, X = [int(x) for x in input().split()]
    items = [int(y) for y in input().split()]
    chng = {}
    freq = {}
    answers = {}
    count = 0
    for item in items:
        chng[item] = 0
        if (item in freq):
            freq[item] += 1
        elif (item not in freq):
            freq[item] = 1
    max1 = max(freq.values())
    if (X == 0):
        print(max1, 0)
        continue
    for item in items:
        if (item ^ X in freq):
            freq[item ^ X] += 1
        elif (item ^ X not in freq):
            freq[item ^ X] = 1
        if (item ^ X in chng):
            chng[item ^ X] += 1
        elif (item ^ X not in chng):
            chng[item ^ X] = 1
    max2 = 1
    maxi = []
    for V, K in freq.items():
        if (max2 < K):
            max2 = K
            maxi.clear()
            maxi.append(V)
        elif (max2 == K):
            max2 == K
            maxi.append(V)
    minchng = 10000000000000000000
    for itm in maxi:
        minchng = min(minchng, chng[itm])
    print(max2, minchng)


