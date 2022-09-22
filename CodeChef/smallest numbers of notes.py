A = [1,2,5,10,50,100]

tes = int(input())
while (tes != 0):
    i = 5
    j = -1
    count = 0
    n = int(input())
    while (n != 0):
        if (A[i] > n):
            i -= 1
        else:
            n = n - A[i]
            count += 1
    print(count)
    tes -= 1