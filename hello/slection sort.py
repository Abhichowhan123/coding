a = [5, 3, 8, 6, 7, 2]
for i in range(len(a)):
    n = i
    for j in range(i,len(a)):
        if a[i] > a[j]:
            n = j
        print(a)

    k = a[i]
    a[i] = a[n]
    a[n] = k
    print(" ")
    print(a)
print(" ")
print(a)