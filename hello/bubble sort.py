def bubble(a):
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                k = a[i]
                a[i] = a[i + 1]
                a[i + 1] = k

        print(a)
a = [15,16,6,8,5,9]
bubble(a)
