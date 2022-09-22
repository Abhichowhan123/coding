numbers = [-1,-1,1,1,1,1,1,1,1,]
target = -2
A = []
for i in range(len(numbers)):
    s = (target- numbers[i])
    l = i+1
    r = len(numbers) - 1
    while l <= r:
        m = (l + r) // 2
        if s == numbers[m]:
            A.append(i+1)
            A.append(m+1)
            break
        if numbers[m] < s:
            l = m + 1
        else:
            r = m - 1
print(A)
